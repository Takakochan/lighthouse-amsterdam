from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('poems/', views.poem_list, name='poem_list'),
    path('poems/<int:pk>/', views.poem_detail, name='poem_detail'),
    path('poems/new/', views.poem_create, name='poem_create'),
    path('poems/<int:pk>/edit/', views.poem_edit, name='poem_edit'),
    path('poems/<int:pk>/delete/', views.poem_delete, name='poem_delete'),
]
