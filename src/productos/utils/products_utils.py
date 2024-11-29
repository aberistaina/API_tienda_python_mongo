from config.mongodb import mongo
from bson import ObjectId

def get_all_utils():
    try:
        all_products = []
        products = mongo.db.productos.find()
        if products:
            for product in products:
                all_products.append({
                "id": str(product["_id"]),  
                "nombre": product["nombre"],
                "marca": product["marca"],
                "descripcion": product["descripcion"],
                "precio": product["precio"],
                "stock": product["stock"]
            })
        else:
            raise ValueError(f"No hay productos en la base de datos")
        return all_products
    
    except Exception as error:
        print(error)
        raise RuntimeError(f"Error al obtener productos: {error}")
    

def get_id_utils(id):
    try:
        product = mongo.db.productos.find_one({
            "_id": ObjectId(id)
        })
        if product:
            product["_id"] = str(product["_id"])
            return product
        else:
            raise ValueError(f"El producto con id {id} no existe en la base de datos")

    except Exception as error:
        print(error)
        raise RuntimeError(f"Error al obtener productos: {error}")
    

def create_utils(data):
    try:
        nombre, marca, descripcion, precio, stock = data["nombre"], data["marca"], data["descripcion"], data["precio"], data["stock"]

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
        return result
    except Exception as error:
        raise RuntimeError(f"Error al crear el producto, el campo {error} no puede estar vacío")


def update_utils(id, data):
    try:
        product = mongo.db.productos.find_one({
            "_id": ObjectId(id)
        })
        if product:
            nombre, marca, descripcion, precio, stock = data["nombre"], data["marca"], data["descripcion"], data["precio"], data["stock"]

            result = mongo.db.productos.update_one(
                    {"_id": ObjectId(id)},  
                    {"$set": {
                        "nombre": nombre,
                        "marca": marca,
                        "descripcion": descripcion,
                        "precio": precio,
                        "stock": stock
                    }})  
            return result
            
        else:
            raise ValueError(f"El producto con id {id} no existe en la base de datos")
        
    except Exception as error:
        print(error)
        raise RuntimeError(f"Error al eliminar el producto: {error}")

def delete_utils(id):
    try:
        product = mongo.db.productos.find_one({
            "_id": ObjectId(id)
        })
        if product:
            product["_id"] = str(product["_id"])

            mongo.db.productos.delete_one({
                "_id": ObjectId(id)
            })
        else:
            raise ValueError(f"El producto con id {id} no existe en la base de datos")

        return product

    except Exception as error:
        print(error)
        raise RuntimeError(f"Error al eliminar el producto: {error}")
    
