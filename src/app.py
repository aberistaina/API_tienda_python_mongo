from flask import Flask
from dotenv import load_dotenv
import os

from config.mongodb import mongo
from productos.routes.productos_routes import productos

load_dotenv()

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo.init_app(app)


app.register_blueprint(productos, url_prefix="/api/v1/productos")
if __name__ == "__main__":
    app.run(debug=True)