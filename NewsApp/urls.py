from django.urls import path
from .views import NewsDate, NewsP, Home, Contact, Register

urlpatterns = [
    path('', Home, name ='Home'),
    path('News/', NewsP, name ='News'),
    path('NewsDate/<int:year>', NewsDate, name ='NewsDate'),
    path('Contact/', Contact, name ='Contact'),
    path('Signup/', Register, name ='Register')
]