from django.shortcuts import render

# Create your views here.
def login_page(request):
    context = {}
    return render(request, 'login/login.html', context)

def signup_page(request):
    context = {}
    return render(request, 'login/signup.html', context)

def forgot_page(request):
    context = {}
    return render(request, 'login/forgot.html', context)

