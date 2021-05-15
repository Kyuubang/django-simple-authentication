from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.index_page, name="index"),
        path('register/', views.register_page, name="register"),
        path('forgot/', views.forgot_page, name="forgot")
        ]
