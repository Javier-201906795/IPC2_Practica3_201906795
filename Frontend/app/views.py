from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
import json

#Endpiont
endpoint = 'http://127.0.0.1:4000/'

def index(request):
    return render(request, 'index.html')

def editar(request):
    try:
        productos = listaproductos()
        #Almacenar 
        contexto = {'productos': productos}

        return render(request, 'editar.html', contexto)
    except Exception as e:
        print('Error en editar()\n',e)

def listaproductos():
    try:
        #obtener del backend
        headers = {'Content-Type': 'application/json'}
        response = requests.get(endpoint, headers=headers)   
        # print(response.status_code, response.text)
        #Convertir en json 
        productos = response.json()
        return productos
    except Exception as e:
        print('Error ne listaproductos()')


def obtenerlista(request):
    try:
        productos = listaproductos()
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

            print(nombre, categoria, descripcion, precio, stock, vencimiento)

            #Back-end crear producto
            try:
                headers = {'Content-Type': 'application/json'}
                data = {
                        "categoria": categoria,
                        "descripcion": descripcion,
                        "nombre": nombre,
                        "precio": precio,
                        "stock": stock,
                        "vencimiento": vencimiento
                        }
                
                url = endpoint + 'agregar'
                print('url ', url)
                response = requests.post(url,json=data,headers=headers)  
                print(response.status_code, response.text)
            except Exception as e:
                print('Error en el backend al agregar producto\n',e)

            return redirect('/')
    
    except Exception as e:
        print('Error en guardar_producto()\n',e)
        return redirect('/editar/')
