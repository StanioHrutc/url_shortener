"""Initialize Flask Application."""
from flask import Flask

from datetime import timedelta


def create_app():
    """Construct the core application."""
    app = Flask(__name__, template_folder="templates")

    with app.app_context():
        app.secret_key = "super_secret_key"
        app.config["SESSION_TYPE"] = "filesystem"
        app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)
        from . import routes
        return app
