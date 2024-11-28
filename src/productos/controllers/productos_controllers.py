from flask import request ,jsonify
from config.mongodb import mongo

def get_all_products():
    try:
        products = []
        for product in mongo.db.productos.find():
            products.append({
                "id": str(product["_id"]),  
                "nombre": product["nombre"],
                "marca": product["marca"],
                "descripcion": product["descripcion"],
                "precio": product["precio"],
                "stock": product["stock"]
            })

        response_data = {
            "data": products,
            "message": "Productos encontrados de manera exitosa",
            "code": 200
        }

        return jsonify(response_data), 200


    except Exception as error:  
        return jsonify({
            "message": f"Ocurrió un error: {str(error)}",
            "code": 500
        }), 500
    

def get_products_id(id):
    return f"All Products {id}"

def create_product():
    try:
        data = request.get_json()
        nombre, marca, descripcion, precio, stock = data["nombre"], data["marca"], data["descripcion"], data["precio"], data["stock"]

        if(nombre, marca, descripcion, precio, stock):
            response = mongo.db.productos.insert_one({
                "nombre": nombre,
                "marca": marca,
                "descripcion": descripcion,
                "precio": precio,
                "stock": stock
            })
            result = {
                "id": str(response.inserted_id),
                "nombre": nombre,
                "marca": marca,
                "descripcion": descripcion,
                "precio": precio,
                "stock": stock
            }

        return jsonify({
            "data": result,
            "message": f"El Producto {nombre} fue creado correctamente",
            "code": 201
        }), 201
    
    except Exception as error:  
        return jsonify({
            "message": f"Ocurrió un error: {str(error)}",
            "code": 500
        }), 500

def update_product(id):
    return f"Producto con id {id} fue modificado"

def delete_product(id):
    return f"Producto con id {id} fue eliminado"
