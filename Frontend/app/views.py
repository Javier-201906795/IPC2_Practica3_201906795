from django.shortcuts import render
import requests
import json

#Endpiont
endpoint = 'http://127.0.0.1:4000/'

def index(request):
    return render(request, 'index.html')

def editar(request):
    return render(request, 'editar.html')

def obtenerlista(request):
    try:
        #obtener del backend
        headers = {'Content-Type': 'application/json'}
        response = requests.get(endpoint, headers=headers)   
        print(response.status_code, response.text)
        #Convertir en json 
        productos = response.json()
        #Almacenar 
        contexto = {'productos': productos}
        #Enviar
        return render(request, 'index.html', contexto)
    except Exception as e:
        print('Error en obtenerlista()\n',e)
        return render(request, 'index.html')



