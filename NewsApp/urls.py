from django.urls import path
from .views import News, Home, Contact

urlpatterns = [
    path('', Home, name ='Home'),
    path('News/', News, name ='News'),
    path('Contact/', Contact, name ='Contact')
]