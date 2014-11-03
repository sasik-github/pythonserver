from django.conf.urls import patterns, url
from django.views.generic.list import ListView
from userregister import views


urlpatterns = patterns('userregister.views',
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^register_form/$', 'register_form', name = 'register'),
)