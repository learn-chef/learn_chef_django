from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from random_images import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^category/(.+)', views.category, name='category'),
)

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
