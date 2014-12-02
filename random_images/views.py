import os, random
from django.conf import settings
from django.core.urlresolvers import resolve
from django.http import Http404
from django.shortcuts import render
from ipware.ip import get_ip
from random_images import categories
from random_images.models import Impression

# returns a random static image
def choose_random_image(images_path):
    image_dir = os.path.join(settings.STATICFILES_DIRS[0], images_path)
    return os.path.join(settings.STATIC_URL, os.path.join(images_path, random.choice(os.listdir(image_dir))))

# handler for image categories
def category(request, category):
    # get path to the images in this category
    images_path = os.path.join(resolve(request.path).namespace + '/images/category', category)

    # select a random image from the images directory
    try:
        image_path =  choose_random_image(images_path)
    except OSError:
        # if image could not be loaded, it likely means that the user
        # entered an invalid URL in the address bar.
        raise Http404()
    image_name = os.path.basename(image_path)

    # get user's IP address
    ip_addr = get_ip(request)

    # add entry to the database
    impression = Impression(ip_addr=ip_addr, image_name=image_name, category=category)
    impression.save()

    # select the count of all views of this image
    view_count = Impression.objects.filter(image_name=image_name).count()

    # render the response
    context = {
        'view_count': view_count, # number of times image was viewed
        'file_path': image_path, # image to display
        'path': request.path, # used to generate link to same page
    }
    return render(request, 'random_images/category.html', context)

# index view
def index(request):
    # create a copy of all categories
    categories_copy = categories.CATEGORIES[:]
    # for each category, insert a field that refers to a random image to show
    for category in categories_copy:
        category['image'] = choose_random_image(os.path.join(resolve(request.path).namespace + '/images/category', category['category']))
    # render the response
    return render(request, 'random_images/index.html', { 'categories': categories_copy })
