from flask import request ,jsonify
from ..utils.products_utils import get_all_utils, create_utils, get_id_utils, delete_utils


def get_all_products():
    try:
        products = get_all_utils()
        print(products)
        response_data = {
            "data": products,
            "message": "Productos encontrados de manera exitosa",
            "code": 200
        }
        return jsonify(response_data), 200


    except Exception as error:  
        return jsonify({
            "message": f"{str(error)}",
            "code": 500
        }), 500
    

def get_products_id(id):
    try:
        result = get_id_utils(id)
        
        return jsonify({
            "data": result,
            "message": "producto encontrado con éxito",
            "code": 200
        }), 200
    
    except Exception as error:  
        return jsonify({
            "message": f"{str(error)}",
            "code": 500
        }), 500


def create_product():
    try:
        data = request.get_json()
        result = create_utils(data)
        
        return jsonify({
            "data": result,
            "message": f"El Producto {result['nombre']} fue creado correctamente",
            "code": 201
        }), 201
    
    except Exception as error:  
        return jsonify({
            "message": f"{str(error)}",
            "code": 500
        }), 500

def update_product(id):
    try:
        data = request.get_json()
        result = create_utils(id, data)
        
        return jsonify({
            "data": result,
            "message": f"El Producto {result['nombre']} fue creado correctamente",
            "code": 201
        }), 201
    
    except Exception as error:  
        return jsonify({
            "message": f"{str(error)}",
            "code": 500
        }), 500

def delete_product(id):
    try:
        result = delete_utils(id)
        
        return jsonify({
            "message": f"El producto con id {id} fue eliminado con éxito",
            "code": 200,
            "data": result
        }), 200
    
    except Exception as error:  
        return jsonify({
            "message": f"{str(error)}",
            "code": 500
        }), 500
