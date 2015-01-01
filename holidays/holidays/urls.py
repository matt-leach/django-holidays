from django.conf.urls import patterns, include, url
from django.contrib import admin

from holidays.views import AddHolidayView, GetYearlyHolidaysView

urlpatterns = patterns('',
    url(r'^add/$', AddHolidayView.as_view(), name='user'),
    url(r'^getYearly/$', GetYearlyHolidaysView.as_view(), name='get_yearly'),
)
