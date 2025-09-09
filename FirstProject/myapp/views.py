from django.http import HttpResponse, JsonResponse


def home(request):
    return HttpResponse("Hello, this is my first Django app!")  
    # URL: http://127.0.0.1:8000/ → Hello, this is my first Django app!

def showname(request, v1, v2):
    return HttpResponse(f"Sum = {v1 + v2}")  
    # URL: http://127.0.0.1:8000/showname/3/5 → Sum = 8

def getval(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    operation = request.GET.get('c')

    try:
        a = float(a)
        b = float(b)

        if operation == 'add':
            return HttpResponse(f"The sum is {a + b}")  
            # URL: http://127.0.0.1:8000/getval?a=10&b=5&c=add -> The sum is 15.0
        elif operation == 'minus':
            return HttpResponse(f"The result is {a - b}")  
            # URL: http://127.0.0.1:8000/getval?a=10&b=5&c=minus -> The result is 5.0
        else:
            return HttpResponse("Invalid operation. Use 'add' or 'minus'.")
    except (ValueError, TypeError):
        return HttpResponse("Invalid Input")

def json(request):
    data = {"name": "Sanuj", "age": 22}
    return JsonResponse(data)
    #http://127.0.0.1:8000/json/    → {"name":"Sanuj","age":22}
 
def apidata(request):
    response = requests.get("https://jsonplaceholder.typicode.com/posts")  # Example public API
    data = response.json()
    return JsonResponse(data, safe=False)
    #External API data: http://127.0.0.1:8000/apidata/

