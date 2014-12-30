from django.views.generic import TemplateView, DetailView, View
from django.contrib.auth.models import User
from django.http import HttpResponse

class HomeView(TemplateView):
    template_name = "core/home.html"
    
    
class UserDetailView(DetailView):
    model = User
    template_name = "core/user_page.html"
    
    
class MeView(View):
    
    def dispatch(self, request):
        return HttpResponse("<p>User</p>")
    