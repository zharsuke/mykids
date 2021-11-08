from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        return render(request, 'index.html')

@login_required(login_url='login')
def homepage(request):
    return render(request, 'homepage.html')

def visi(request):
    return render(request, 'visi.html')

def cara(request):
    return render(request, 'cara.html')

def syarat(request):
    return render(request, 'syarat.html')