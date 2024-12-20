from flask import Flask, render_template
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

    from app.stupid import stupid_bp
    app.register_blueprint(stupid_bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    return app
