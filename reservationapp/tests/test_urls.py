from django.test import SimpleTestCase
from django.urls import resolve,reverse 
from reservationapp.views import availability

class TestUrls(SimpleTestCase):
    def test_availability_url_resolved(self):
        url = reverse('availability')
        self.assertEquals(resolve(url).func,availability)
