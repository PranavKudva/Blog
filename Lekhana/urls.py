from Lekhana import settings
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('', url(r'^home/$', TemplateView.as_view(template_name='writeBlog.html')),
                       (r'post/', 'core.views.post'),
                       (r'search/', 'core.views.search'),
                       (r'view/', 'core.views.view'),
                       (r'manip/','core.views.manip'),
                       (r'update/','core.views.update'),
    (r'resources/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT})
)