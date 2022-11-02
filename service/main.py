"""Initialize Flask Application."""
from flask import Flask


def create_app():
    """Construct the core application."""
    app = Flask(__name__, template_folder="templates")

    with app.app_context():
        app.secret_key = "super_secret_key"
        app.config["SESSION_TYPE"] = "filesystem"
        from . import routes
        return app
