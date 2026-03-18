from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('genre/<slug:slug>/', views.recommendations, name='recommendations'),
]
