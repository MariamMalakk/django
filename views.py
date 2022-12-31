from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("hello")


def home(request):
    booksinfo = [
        {"id": 1, "name": "book1", "description": "book1_description"},
        {"id": 2, "name": "book2", "description": "book2_description"},
        {"id": 3, "name": "book3", "description": "book3_description"}]
    return render(request,"books/home.html", context={"books": booksinfo})

def contact(request):
     return render(request, "books/contactus.html")

def about(request):
    return render(request , "books/aboutus.html")