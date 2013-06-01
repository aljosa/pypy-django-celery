from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'testapp.views.home', name='home'),
)
