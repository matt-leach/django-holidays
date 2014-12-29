from django.test import TestCase
from django.contrib.auth.models import User

class TestHomeView(TestCase):
    
    def test_can_always_view_home_page(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        
class TestUserView(TestCase):
    
    def test_create_and_view_user(self):
        u = User.objects.create(username="user")
        resp = self.client.get("/user/%s/" % u.id)
        self.assertEqual(resp.status_code, 200)
        
    def test_no_user_gives_404(self):
        self.assertRaises(User.DoesNotExist, User.objects.get, id=100000)
        resp = self.client.get("/user/100000/")
        self.assertEqual(resp.status_code, 404)