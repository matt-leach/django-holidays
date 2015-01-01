from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from core import views as core_views
urlpatterns = patterns('',
    # Login/logout views
    url(r'^login/$', core_views.login, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    
    # Main page showing user's information - requires login
    url(r'^$', login_required(redirect_field_name=None)(core_views.HomeView.as_view()), name="home"),
    
    # Holiday views
    url(r'^holidays/', include('holidays.urls')),
    
    # Admin view
    url(r'^admin/', include(admin.site.urls)),
)
