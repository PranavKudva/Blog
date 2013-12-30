from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from Blog import settings

# from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'home/', TemplateView.as_view(template_name='index.html'))
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)