from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import CreateUserForm, CreateRegistrosForm, PersonaForm

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('ingresar_registros')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'La cuenta fue creada para ' + user)
				return redirect('login')
		context = {'form':form}
		return render(request, 'registro/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('ingresar_registros')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('ingresar_registros')
			else:
				messages.info(request, 'La contraseña o el usuario no son correctos')

		context = {}
		return render(request, 'registro/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
	registros = Registro.objects.all()
	return render(request, 'registro/home.html', {'registros': registros})
	

@login_required(login_url='login')
def registros(request):
    registros = Registro.objects.all()
    return render(request, 'registro/listar_registros.html', {'registros': registros})

@login_required(login_url='login')
def CreateRegistros(request):
	form = CreateRegistrosForm()
	if request.method == 'POST':
		form = CreateRegistrosForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('listar_registros')
	context = {'form':form}
	return render(request, 'registro/ingresar_registros.html', context)

@login_required(login_url='login')
def MantenedorPersonas(request):
    personas = Persona.objects.all()
    return render(request, 'registro/mantenedor_personas.html', {'personas': personas})

@login_required(login_url='login')
def createPersona(request):
	form = PersonaForm()
	if request.method == 'POST':
		form = PersonaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('mantenedor_personas')
	context = {'form':form}
	return render(request, 'registro/personas_form.html', context)

@login_required(login_url='login')
def updatePersona(request, pk):
	persona = Persona.objects.get(rut=pk)
	form = PersonaForm(instance=persona)
	if request.method == 'POST':
		form = PersonaForm(request.POST, instance=persona)
		if form.is_valid():
			form.save()
			return redirect('mantenedor_personas')
	context = {'form':form}
	return render(request, 'registro/personas_form.html', context)

@login_required(login_url='login')
def deletePersona(request, pk):
	persona = Persona.objects.get(rut=pk)
	if request.method == "POST":
		persona.delete()
		return redirect('mantenedor_personas')

	context = {'item':persona}
	return render(request, 'registro/eliminar.html', context)