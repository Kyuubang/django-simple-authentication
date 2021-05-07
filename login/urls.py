from django.urls import path
from . import views

urlpatterns = [
        path('', views.index_page, name="index"),
        path('login/', views.login_page, name="login"),
        path('register/', views.signup_page, name="register"),       
        path('forgot/', views.forgot_page, name="forgot")
        ]
