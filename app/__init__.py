from flask import Flask, Blueprint
from instance.config import app_config


def create_app():
    app = Flask(__name__, instance_relative_config=True)
   

    from .api.v1 import version1
    app.register_blueprint(version1)

    
    return app