from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home_view(request):
    ctx = {
        'user': request.user
    }

    return render(request, 'home.html', ctx)

def login_view(request):
    pass

def logout_view(request):
    pass