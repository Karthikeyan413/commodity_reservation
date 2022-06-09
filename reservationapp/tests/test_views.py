from django.test import TestCase, Client
from django.urls import reverse
from reservationapp.models import Route,Train,Time
from django.contrib.auth.models import User
import json

class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@email.com', 'testtest')
        self.client.force_login(self.user)

    def test_avaliability_GET(self):

        response = self.client.get(reverse('availability'))

        self.assertEquals(response.status_code,200)

        self.assertTemplateUsed(response, 'reservation.html')
    def test_reservation_POST(self):
        
        response = self.client.post(reverse('availability'),{
            'source' : 'chnai',
            'destination': 'madurai',
            'type': 'coal',
        })
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'availability.html')
