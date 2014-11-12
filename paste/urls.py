from django.conf.urls import patterns, url

from paste import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add/$', views.add, name='add'),
    url(r'^delete/(?P<delete_hash>\w+)/$', views.delete, name='delete'),
    url(r'^(?P<url_hash>\w+)(/(?P<theme_name>\w+))?/$', views.view, name='view'),
)
