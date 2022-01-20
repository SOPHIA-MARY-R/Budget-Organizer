from django.urls import path
from . import views

urlpatterns=[
    path('', views.ecreate, name='ecreate'),
    path('eselect/', views.eselect, name='eselect'),
    path('eedit/<int:id>', views.eedit, name='eedit'),
    path('edelete/<int:id>', views.edelete, name='edelete'),
]