from django.shortcuts import render
import requests
import json

#Endpiont
enpointlista = 'http://127.0.0.1:4000/'

def index(request):
    return render(request, 'index.html')

def obtenerdatoscrear(request):
    try:
        if request.method == 'POST':
            form = editar(request.POST)
            if form.is_valid():
                nombre = form.cleaned_data['crearNombre']
                print(nombre)
        
        return render(request, 'index.html')
    except Exception as e:
        return None

def editar(request):
    return render(request, 'editar.html')