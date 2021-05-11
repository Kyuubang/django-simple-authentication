from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import NameForm

# Create your views here.
def index_page(request):
    form = NameForm()
    context = {
            'form': form,
            }
    return render(request, 'login/index.html', context)

def login_page(request):
    context = {}
    return render(request, 'login/login.html', context)

def signup_page(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return redirect('login')
    else:
        form = NameForm()
    return render(request, 'login/signup.html', context)

def forgot_page(request):
    context = {}
    return render(request, 'login/forgot.html', context)

