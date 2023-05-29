from django import forms
from todoapp.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Empform(forms.Form):

    empno=forms.FloatField()
    name=forms.CharField(max_length=50)
    job=forms.CharField(max_length=50)
    salary=forms.FloatField()
    city=forms.CharField(max_length=20)
    age=forms.FloatField()

    #data members defined in the form class become form fields

class ProductForm(forms.ModelForm):

     name=forms.CharField(max_length=50)
     pdesc=forms.CharField(max_length=100)
     price=forms.FloatField()

     class Meta:
        model=Product
        fields=['name','pdesc','price']

class RegisterForm(UserCreationForm):

    class Meta:
        model=User
        fields=['username','first_name','last_name','email']