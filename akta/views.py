from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import *

# Create your views here.

@login_required(login_url='login')
def buat(request):
    return render(request, 'create.html')

@login_required(login_url='login')
def detail(request):
    return render(request, 'detail.html')

@login_required(login_url='login')
def akta(request):
    akta = Akta.objects.filter(user=request.user)
    context = {'akta' : akta}
    return render(request, 'akta.html', context)