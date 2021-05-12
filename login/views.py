from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# custom forms (forms.py)
from .forms import UserRegister

# Create your views here.
#@login_required(login_url='login')
def index_page(request):
    # form = UserRegister()
    # context = {
    #         'form': form,
    #         'username': "Bayhaqi",
    #         }
    context = {}
    return render(request, 'accounts/index.html', context)

def login_page(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def register_page(request):
    # if request.method == "POST":
    #     form = UserRegister(request.POST)
    #     if form.is_valid():
    #         return redirect('login')
    # else:
    #     form = UserRegister()
    # form = UserRegister()

    form = UserRegister()

    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
        else:
            form.send_same_password_message()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/register.html', context)

def forgot_page(request):
    context = {}
    return render(request, 'login/forgot.html', context)

