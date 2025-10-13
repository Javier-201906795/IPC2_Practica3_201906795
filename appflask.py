from flask import Flask, request, render_template, redirect, url_for
from flask_cors import CORS
from flask.json import jsonify

#Crear app
app = Flask(__name__)
#CORS
cors = CORS(app)



app.config['DB'] = [{
        "nombre": "Manzanas Gala",
        "categoria": "Frutas",
        "descripcion": "Manzanas frescas y crujientes, ideales para snacks saludables o postres.",
        "precio": 12.50,
        "stock": 85,
        "vencimiento": "2025-11-15"
    },
    {
        "nombre": "Bananas",
        "categoria": "Frutas",
        "descripcion": "Bananas dulces y maduras, ideales para batidos o desayunos.",
        "precio": 8.00,
        "stock": 120,
        "vencimiento": "2025-11-10"
    }]



@app.route('/',   methods=['GET','POST'])
def inicio():
    try:
        baseDatos = app.config['DB']
        return jsonify(baseDatos) 
    except Exception as e:
        print('!!! Error FLASK inicio() !!!\n',e)


@app.route('/editar/<string:nombre>',   methods=['GET','PUT'])
def editar(nombre):
    try:
        baseDatos = app.config['DB']
        data = request.get_json()  # datos enviados en formato JSON

        # Buscar el producto en la base de datos
        for producto in baseDatos:
            if producto["nombre"].lower() == nombre.lower():
                print("Producto encontrado:", producto)
                # Actualizar los campos recibidos y si no fue enviado el dato colocar el valor anterior
                producto.update({
                    "nombre": data.get("nombre", producto["nombre"]),
                    "categoria": data.get("categoria", producto["categoria"]),
                    "descripcion": data.get("descripcion", producto["descripcion"]),
                    "precio": data.get("precio", producto["precio"]),
                    "stock": data.get("stock", producto["stock"]),
                    "vencimiento": data.get("vencimiento", producto["vencimiento"])
                })
                return jsonify({
                    "mensaje": f"Producto '{nombre}' actualizado correctamente.",
                    "producto": producto
                }), 200

        # Si no se encuentra el producto
        return jsonify({"error": f"Producto '{nombre}' no encontrado."}), 404

    except Exception as e:
        print("!!! Error FLASK editar_producto() !!!\n", e)
        return jsonify({"error": "Error interno en el servidor"}), 500



#Ejecutar
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 4000, debug=True)
