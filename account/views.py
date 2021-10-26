from django.shortcuts import render, redirect
from . import views
from django.contrib.auth.forms import UserCreationForm
from .forms import Usercreate
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout


# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('homepage')
            else:
                messages.info(request, 'username atau password salah')

        context = {}
        return render(request, 'login.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = Usercreate()

        if request.method == 'POST':
            form = Usercreate(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Akun berhasil dibuat. Selamat datang ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'register.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')