from django.urls import path
from .views import NewsDate, NewsP, Home, Contact, Register, addUser,modalForm, addModalForm

urlpatterns = [
    path('', Home, name ='Home'),
    path('News/', NewsP, name ='News'),
    path('NewsDate/<int:year>', NewsDate, name ='NewsDate'),
    path('Contact/', Contact, name ='Contact'),
    path('Signup/', Register, name ='Register'),
    path('addUser/', addUser, name ='addUser'),
    path('modalForm/', modalForm, name ='form'),
    path('addModalForm/', addModalForm, name ='modalForm')
]