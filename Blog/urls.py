from Blog import settings
from django.conf.urls import patterns, url

# from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('', url(r'home/', TemplateView.as_view(template_name='createBlog.html')),
    (r'bootstrap/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT})
)