from django.views.generic import TemplateView, DetailView
from django.contrib.auth.models import User


class HomeView(TemplateView):
    template_name = "core/home.html"
    
class UserDetailView(DetailView):
    model = User
    template_name = "core/user_page.html"