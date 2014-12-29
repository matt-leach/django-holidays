from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import HomeView, UserDetailView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user'),
)
