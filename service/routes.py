"""Route declaration."""
import uuid

from flask import current_app as app
from flask import (
    render_template, redirect,
    request, url_for,
    session
)

from service.db.db import DBHandler
from service.utils.url_shortener import generate_random_short_url


@app.route("/")
def home():
    """Intro login page."""
    if not session.get("username"):
        name = str(uuid.uuid4())[:10]
        DBHandler.create_new_user(name)
        session["username"] = name

    return redirect(url_for("main"))


@app.route("/main")
def main():
    """Main page for URL shortening"""
    current_user = session.get("username")
    if not current_user:
        print("redirecting to home")
        return redirect(url_for("home"))

    records = list(DBHandler.get_records(current_user))
    return render_template(
        "main.html",
        title="URL Shortene",
        username=current_user,
        records=records,
        description="Smarter page templates with Flask & Jinja."
    )


@app.route("/generate", methods=["POST"])
def generate():
    """Endpoint for generating short url and saving records to DB."""
    original_url = request.form.get("url")
    short_url = generate_random_short_url()

    try:
        DBHandler.create_url_record(original_url, short_url)
    except:
        # Usually cases with the same URL creation
        # skipping such errors for simplicity
        pass

    try:
        DBHandler.create_user_url_mapping(session.get("username"), original_url)
    except:
        # Usually cases with the same URL creation
        # skipping such errors for simplicity
        pass

    return redirect(url_for("main"))


@app.route("/update_counter", methods=["POST"])
def update_counter():
    """Endpoint for updating click counter."""
    pair_id = request.form.get("pair")
    DBHandler.update_user_click_information(pair_id)
    return redirect(url_for("main"))
