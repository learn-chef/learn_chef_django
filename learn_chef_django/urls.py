from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/random_images', permanent=False)), # redirect root to /random_images
    url(r'^random_images/', include('random_images.urls', namespace='random_images')),
    url(r'^admin/', include(admin.site.urls)),
)
