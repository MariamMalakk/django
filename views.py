from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from books.models import booklib
# Create your views here.
def hello(request):
    return HttpResponse("hello")


# def home(request):
#     booksinfo = [
#         {"id": 1, "name": "book1", "description": "book1_description"},
#         {"id": 2, "name": "book2", "description": "book2_description"},
#         {"id": 3, "name": "book3", "description": "book3_description"}]
#     return render(request,"books/home.html", context={"books": booksinfo})

def getbook(request):
    book = booklib.objects.all()
    return render(request, "books/home.html" , context={"books":book} )

def showbooks(request , id):
     booksh = get_object_or_404(booklib ,pk=id )
     return render(request, "books/showbooks.html", context={"book":booksh})

def deletebook(request ,id):
    bookdel = booklib.objects.get(id=id)
    bookdel.delete()
    return redirect ("books")

def contact(request):
     return render(request, "books/contactus.html")

def about(request):
    return render(request , "books/aboutus.html")