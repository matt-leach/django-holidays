from django.test import TestCase


class TestHomeView(TestCase):
    
    def test_can_always_view_home_page(self):
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)