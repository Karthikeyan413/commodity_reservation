from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class UserCredientials(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_no = models.IntegerField(null=False, blank=False, unique=True)
#     railway_devision = models.CharField()
#     document = models.
#     def __str__(self):
#         return self.user.username

'''
class CompanyInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=20, null=False, blank=False)
    company_type = models.PositiveIntegerField()
    company_address = models.DateField()
    GSTIN_no = 
    CIN_no = 
    PinCode = 

    def __str__(self):
        return str(self.patient_name) + " " + str(self.patient_age) + " " + str(self.patient_DOB)
        '''