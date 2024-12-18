from flask import Flask
import os
from dotenv import load_dotenv

load_dotenv()


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev')
    )
    app.config.from_pyfile('config.py')
    app.config.from_prefixed_env()

    # Blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app
