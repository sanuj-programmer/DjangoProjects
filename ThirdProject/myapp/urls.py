from django.urls import path
from . import views

urlpatterns = [
    path('', views.name, name='name'),
    path('about/', views.about),
]