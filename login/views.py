import random

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# custom forms (forms.py)
from .forms import UserRegister

# Create your views here.
#@login_required(login_url='login')
def index_page(request):
    greetings = random.choice([
        'Hello',
        'Hi',
        'Hola',
        "Assalamu'alaikum",
        'Bonjour',
        'Ciao',
        'OLÀ',
        'ZDRAS-TVUY-TE',
        'Ohayo',
        'Marhaba',
        'Ni Hau',
        'Halo',
        'Guten Morgen',
        'Danke',
        'Salam',
    ])

    context = {
        'greetings' : greetings,
    }
    return render(request, 'registration/index.html', context)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = UserRegister()
        if request.method == 'POST':
            form = UserRegister(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {
            'form' : form,
        }
        return render(request, 'registration/register.html', context)

def forgot_page(request):
    context = {}
    return render(request, 'registration/forgot.html', context)

def custom_404_view(request, exception):
    return render(request, '404.html')


