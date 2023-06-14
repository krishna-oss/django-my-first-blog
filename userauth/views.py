from django.shortcuts import render
from django.contrib.auth import login, logout

# Create your views here.

def login_user(request):
     
     return render(request,'login.html')

def register_user(request):
#   if request.method=='POST':
     
     return render(request,'register.html')