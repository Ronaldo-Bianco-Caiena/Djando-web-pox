from django.shortcuts import render, redirect
from .models import News, RegistrationData
from .forms import RegistrationForm,RegistrationModal
from django.contrib import messages
# Create your views here.

def Home(request):
    context = {
        "name":"Ronaldo bianco"
    }
    return render(request,'home.html', context)

def NewsP(request):
    obj = News.objects.get(id=1)
    context = {
        "data":obj
    }
    return render(request,'news.html',context)

def NewsDate(request, year):

    article_list = News.objects.filter(pub_date__year = year)
    context = {
        'year':year,
        'article_list':article_list
    }

    return render(request, 'newsDate.html',context)

def Contact(request):
    return render(request,'contact.html')

def Register(request):

    context = {
        "form": RegistrationForm
    }

    return render(request,'signup.html', context)

def addUser(request):
    form = RegistrationForm(request.POST)

    if form.is_valid():
        myregister = RegistrationData(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password'],
            email = form.cleaned_data['email'],
            phone = form.cleaned_data['phone']
        )
        myregister.save()
        messages.add_message(request, messages.SUCCESS, "Congratulations you have signed up successfully")
    return redirect('Register')

def modalForm(request):

    context = {
        "modalForm": RegistrationModal
    }

    return render(request, 'modalForm.html', context)

def addModalForm(request):
    myModalForm = RegistrationModal(request.POST)

    if myModalForm.is_valid():
        myModalForm.save()
    return redirect('Home')
