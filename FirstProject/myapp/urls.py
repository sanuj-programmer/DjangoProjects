from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('showname/<int:v1>/<int:v2>/', views.showname),
    path('getval/', views.getval),
    path('json/', views.json),
    path('apidata/', views.apidata),
]




