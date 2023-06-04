from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You've succesfully been succesfully logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging you in, please try again!")
            return redirect('home')
    else:
        return render(request, 'home.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')