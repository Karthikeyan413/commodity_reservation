from django.test import TestCase
from reservationapp.models import Train,Route,Time
 

class TestModels(TestCase):
    def setUp(self):
        self.train1= Train.objects.create(
            train_name = 'Train10',
            train_id = 10,
            no_of_block = 25,
            type = 'Covered',
            availability = False,
        )
    def test_model_check(self):
        self.assertEquals(self.train1.train_name, 'Train10')