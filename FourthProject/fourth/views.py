from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# def home(request):
#   return HttpResponse("Hello World!")

# def about(request):
#   return HttpResponse("About Page")


# def home(request):
#   return render(request, 'index.html')



def home(request):
    students = [
        {"name": "Alice"},
        {"name": "Bob"},
        {"name": "Charlie"},
    ]
    context = {
        "age": 20,
        "students": students
    }
    return render(request, "index.html", context)

def about(request):
    return render(request, "about.html")
