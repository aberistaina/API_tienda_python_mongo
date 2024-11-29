from flask import Blueprint
from productos.controllers.productos_controllers import get_all_products, get_products_id, update_product, delete_product, create_product


productos = Blueprint("productos", __name__)

@productos.route("/", methods=["GET"])
def get_all():
    return get_all_products()

@productos.route("<string:id>", methods=["GET"])
def get_id(id):
    return get_products_id(id)

@productos.route("/", methods=["POST"])
def create():
    return create_product()

@productos.route("<string:id>", methods=["PUT"])
def update(id):
    return update_product(id)

@productos.route("<string:id>", methods=["DELETE"])
def delete(id):
    return delete_product(id)