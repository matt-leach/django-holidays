from django.conf.urls import patterns, include, url
from django.contrib import admin
from holidays.views import AddHolidayView

urlpatterns = patterns('',
    url(r'^add/$', AddHolidayView.as_view(), name='user'),
)
