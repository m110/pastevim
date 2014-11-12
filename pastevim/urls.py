from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^paste/', include('paste.urls', namespace='paste')),
    url(r'^admin/', include(admin.site.urls)),
)
