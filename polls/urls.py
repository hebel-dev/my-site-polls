from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('endex/', views.endex, name='endex'),
]