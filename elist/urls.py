from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.Insert, name='create'),
    path('select/', views.select, name='select'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('createincome/', views.InsertIncome, name='createincome'),
    path('selectincome/', views.selectIncome, name='selectincome'),
    path('editincome/<int:id>/', views.editIncome, name='editincome'),
    path('deleteincome/<int:id>/', views.deleteIncome, name='deleteincome'),
    path('chart/', views.chart, name='chart'),
]

