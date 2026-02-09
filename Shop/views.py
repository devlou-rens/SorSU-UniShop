# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'Shop/base.html')

def login_view(request):
    return render(request, 'Shop/login.html')
