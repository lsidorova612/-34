from flask import Flask
from .models import db, migrate
from . import views


def create_app():
    app = Flask(__name__)
    
    app.config["SECRET_KEY"] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"

    db.init_app(app)
    migrate.init_app(app, db)

    app.add_url_rule("/", view_func=views.index_page)

    return app