from django.views.generic import TemplateView, DetailView, View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.views import login as dj_login

def login(request):
    if request.user.is_authenticated():
        # User is already logged in
        return redirect("/")
    
    return dj_login(request, template_name="core/login.html")


class HomeView(TemplateView):
    template_name = "core/home.html"
    
    
class UserDetailView(DetailView):
    model = User
    template_name = "core/user_page.html"
    
    
class MeView(View):
    
    def dispatch(self, request):
        return HttpResponse("<p>User</p>")
    