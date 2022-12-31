
from django.urls import path
from books.views import home , hello , contact ,about
urlpatterns = [
         # path('home', home, name="home"),
         path('home', home , name="books"),
         path('hello',hello , name="hello"),
         path('contactus' , contact , name="contact"),
         path('about', about ,name="about")

 ]
