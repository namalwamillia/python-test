from flask import Flask
from flask_migrate import Migrate
from authors_app.extensions import db, migrate
from authors_app.controllers.auth.auth_controller import auth
from authors_app.controllers.auth.company_controller import company
from authors_app.controllers.auth.book_controller import books
from authors_app.models.user import MyUser

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(auth, url_prefix="/api/v1/auth")
    app.register_blueprint(company, url_prefix="/api/v1/company")
    app.register_blueprint(books, url_prefix="/api/v1/books")

    @app.route('/')
    def home():
        return "Hello world!"

    return app
