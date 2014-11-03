from django.conf.urls import patterns, url

urlpatterns = patterns('books.views',
    url(r'^search-form/$', 'search_form'),
    url(r'^search/$', 'search'),
)