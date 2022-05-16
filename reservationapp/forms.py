from django import forms
from django.contrib.auth.models import User
from reservationapp.models import UserCredientials,Ticket,Time,Train,Route
from django.core import validators


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input',
            'placeholder': 'Username',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control input',
            'placeholder': 'user@mail.com',
        }
    ))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control input',
        }
    ))

    class Meta():
        model = User
        fields = ['username', 'password', 'email']

class RegisterNoForm(forms.ModelForm):
    phone_no = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control input',
            'placeholder': 'Phone Number',
        }
    ))
    address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control input',
        'placeholder': 'Address',
        'rows' : 2,
    }))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control input',
        'placeholder': 'Age',
    }))
    gender = forms.CharField(widget=forms.CheckboxInput(
        attrs={
            'class': 'form-select',
            'placeholder': 'Gender',
        }
    ))
    class Meta():
        model = UserCredientials
        fields = ('phone_no','address','age','gender',)