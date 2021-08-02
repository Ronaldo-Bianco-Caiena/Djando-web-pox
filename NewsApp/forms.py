from django import forms
from django.forms import widgets
from django.forms.fields import CharField
from .models import RegistrationData

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

class RegistrationModal(forms.ModelForm):
    class Meta:
        model = RegistrationData

        fields = {
            'username',
            'password',
            'email',
            'phone'
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
        }