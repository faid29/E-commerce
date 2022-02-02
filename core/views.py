from django import contrib
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import *

from .forms import ContactoMensaje, Registroform
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#aqui se crean las vistas lo que pide y devuelve el renderizado

def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "core/index.html", context)

def nosotros_de(request):
    return render(request, "core/other/nosotros.html")    

def entrar(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username= nombre_usuario, password = password)

            if usuario is not None:
                login(request, usuario)
                messages.success(request, "Los datos son incorrecto")
                return redirect("index")
            else:
                messages.error(request, f"Bienvenido {nombre_usuario} ")
        else:
            messages.error(request, "Los datos son incorrecto")

    form = AuthenticationForm()
    return render(request, "core/other/login.html", {'form': form}) 

def carrito(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request,"core/other/carrito.html", context)

def registrarse(request):
    if request.method == 'POST':
        form = Registroform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('entrar')
    else:
        form = Registroform()
    return render(request, 'core/other/registro.html', {'form': form})

def salir(request):
    logout(request)
    messages.success(request, f"Cerraste sesión")
    form = AuthenticationForm()
    return render(request, "core/other/login.html", {'form': form})

def contacto(request):
    if request.method == "POST":
        formulario = ContactoMensaje(request.POST)

        if formulario.is_valid():
            return HttpResponseRedirect(reverse("index"))
    else:
        formulario = ContactoMensaje()

        contexto = {'formulario': formulario}
    return render(request, 'core/other/contacto.html', contexto)

def vista_producto(request, product_id):
    products = Product.objects.filter(id=product_id)

    context = {'products': products}
    return render(request,"core/other/vista_producto.html", context)

    #if request.method == "POST":
    #products= Product.objects.get(pk=id)
    #context = { 'products': products}
    #return HttpResponseRedirect(reverse(context))

def galeria_dos(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "core/other/galeria/galeria2.html", context)

