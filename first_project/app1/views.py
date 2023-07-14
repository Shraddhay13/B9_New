from django.shortcuts import render, HttpResponse

# Create your views here.

print("In views.py")

def welcome_func(request):  # reserved --func based view
    # request.GET -- query parameters -- only n only GET request
    # print(request.method)  # http request
    # print(request.user)   #AnonymousUser
    # print(dir(requests))
    # print(request.build_absolute_uri())  # http://127.0.0.1:8000/welcome/
    # print(request.GET.get("Book_Title"))  # <QueryDict: {}>  # {'name': ['abc]}

    # return HttpResponse("<h1>Welcome to our application..!</h1><br><h5>Hi</h5>")
    return render(request, "home.html")
