from django.http import HttpResponse
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


def guardar_producto(request):
    try:
        if request.method == 'POST':
            nombre = request.POST.get('nombre')
            categoria = request.POST.get('categoria')
            descripcion = request.POST.get('descripcion')
            precio = request.POST.get('precio')
            stock = request.POST.get('stock')
            vencimiento = request.POST.get('vencimiento')

            # Aquí puedes guardar el producto en la base de datos o procesarlo
            print(nombre, categoria, descripcion, precio, stock, vencimiento)

            # Ejemplo simple: redirigir a la página principal con mensaje
            return HttpResponse(f"Producto '{nombre}' guardado correctamente.")
    
        return HttpResponse("Método no permitido", status=405)
    except Exception as e:
        print('Error en obtenerlista()\n',e)
        return render(request, 'index.html')
