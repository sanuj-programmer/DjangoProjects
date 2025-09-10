# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def name(request):
    return HttpResponse("I am Sanuj")

def about(request):
    return HttpResponse("This is about page")
