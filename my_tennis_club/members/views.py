from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Add the return statement

        else:
             return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'login.html')
def home_page(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')
