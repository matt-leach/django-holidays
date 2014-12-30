from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import HomeView, UserDetailView, MeView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'core/login.html'}),
    url(r'^user/$', MeView.as_view(), name='me'),
    url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user'),
)
