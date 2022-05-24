# Desde fuera del sistema
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

# Del Sistema
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']

class CreateRegistrosForm(ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'
        widgets = {
            'rut': forms.TextInput(attrs={'class':'form-control text-uppercase','placeholder':'EJ: 20.243.554-0','id':'rut','name':'rut'}),
        }

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'rut': forms.TextInput(attrs={'class':'form-control text-uppercase','placeholder':'EJ: 20.243.554-0','id':'rut','name':'rut'}),
            'nombre': forms.TextInput(attrs={'class':'form-control text-capitalize'}),
            'correo': forms.EmailInput(attrs={'class':'form-control text-lowercase'}),
            'tipo': forms.Select(attrs={'class':'form-control'})
            }