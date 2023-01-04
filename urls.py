
from django.urls import path
from books.views import getbook, hello , contact ,about , showbooks ,deletebook
urlpatterns = [
         # path('home', home, name="home"),
         path('home', getbook , name="books"),
         path('hello',hello , name="hello"),
         path('contactus' , contact , name="contact"),
         path('about', about ,name="about"),
         path('home/show/<int:id>', showbooks , name="show"),
         path('home/delete/<id>', deletebook ,name="del")

 ]
