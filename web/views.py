from django.shortcuts import render, redirect
from web.models import *

def login(request):
    return render(request, "login.html")

def inicio(request):
    datos = Organizacion.objects.all()
    return render(request, "inicio.html",{'datos':datos})

def eliminar(request, id):
    elemento = Organizacion.objects.filter(pk=id).first()
    elemento.delete()
    return redirect('index')

def agregar(request, id):
    pass

def descargar(request, id):
    pass