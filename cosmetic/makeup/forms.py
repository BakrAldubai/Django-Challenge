from django import forms
from .models import Brand,Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']










