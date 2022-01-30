from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request,'makeup/index.html')


def home():
    pass


def products():
    pass


def brands():
    pass


