from flask import Flask
from .config import Config
from .adapters.http import bp as users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Aqui puedo agregar blueprints, rutas, etc
    app.register_blueprint(users_bp)
    return app
