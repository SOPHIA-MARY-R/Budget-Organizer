from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns=[
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('index/', views.index, name='index'),
    path('logout/', auth.LogoutView.as_view(template_name='home.html'), name='logout'),
]