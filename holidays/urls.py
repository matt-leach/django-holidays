from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from core.views import HomeView

urlpatterns = patterns('',
    # Login/logout views
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'core/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
    
    # Main page showing user's information - requires login
    url(r'^$', login_required(redirect_field_name=None)(HomeView.as_view()), name="home"),
    
    # Holiday views
    url(r'^holidays/', include('holidays.urls')),
    
    # Admin view
    url(r'^admin/', include(admin.site.urls)),
)
