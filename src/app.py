from flask import Flask
from productos.routes.productos_routes import productos

app = Flask(__name__)


app.register_blueprint(productos, url_prefix="/api/v1/productos")
if __name__ == "__main__":
    app.run(debug=True)