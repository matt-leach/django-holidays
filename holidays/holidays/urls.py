from django.conf.urls import patterns, include, url
from django.contrib import admin

from holidays.views import add_holiday, GetYearlyHolidaysView

urlpatterns = patterns('',
    url(r'^add/$', add_holiday, name='submit-holiday'),
    url(r'^getYearly/$', GetYearlyHolidaysView.as_view(), name='get_yearly'),
)
