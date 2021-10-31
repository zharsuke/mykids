from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import *
from . forms import *

# Create your views here.

@login_required(login_url='login')
def buat(request):

    form = AktaForm(request.POST, files=request.FILES)

    context = {'form' : form
}
    if request.method == 'POST':
        if form.is_valid():
            pass
            data = form.save(commit=False)
            data.user = User.objects.get(username=request.user)
            data.save()
            return redirect('homepage')
        else:
            print(form.errors)

    return render(request, 'create.html', context)

@login_required(login_url='login')
def detail(request, slug):
    akta = Akta.objects.get(slug=slug)
    context = {'akta' : akta}
    return render(request, 'detail.html', context)

@login_required(login_url='login')
def akta(request):
    akta = Akta.objects.filter(user=request.user)
    context = {'akta' : akta}
    return render(request, 'akta.html', context)