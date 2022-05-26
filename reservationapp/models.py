from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserCredientials(models.Model):
    genders = (
        ('M','male'),
        ('F','female'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=30,null =False, blank=False)
    age = models.PositiveIntegerField(null=False, blank=False)
    gender = models.CharField(max_length=6,choices = genders, null =False, blank=False)
    def __str__(self):
        return self.user

class Train(models.Model):
    train_name = models.CharField(max_length=30,null =False, blank=False)
    train_id = models.IntegerField(primary_key=True)
    no_of_block = models.IntegerField(null =False, blank=False)
    type = models.CharField(max_length=10,blank=False)
    availability = models.BooleanField(null =False, blank=False,default=False)

class Commodity(models.Model):
    type = models.CharField(max_length=20,primary_key=True)

class Route(models.Model):
    train_id = models.ForeignKey('Train',default=1,on_delete=models.CASCADE)
    source = models.CharField(max_length=20,blank=False)
    destination = models.CharField(max_length=20,blank=False)


class Time(models.Model):
    dept_date = models.DateField()
    arrival_date = models.DateField()
    dept_time = models.TimeField()
    arrival_time = models.TimeField()
    train_id = models.ForeignKey('Train',default=1,on_delete=models.CASCADE)


class Ticket(models.Model):
    ticket_num = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User,default=1 ,on_delete=models.CASCADE)
    train_id = models.ForeignKey('Train',default=1,on_delete=models.CASCADE)
    type = models.ForeignKey('Commodity',default=1,on_delete=models.CASCADE)
    block_no = models.IntegerField(null =False, blank=False)
