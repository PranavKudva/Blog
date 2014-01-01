from Blog import settings
from django.conf.urls import patterns, url

# from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('', url(r'^home/$', 'core.views.write_blog'),
                       (r'post_the_blog/', 'core.views.post_blog'),
    (r'resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT})
)