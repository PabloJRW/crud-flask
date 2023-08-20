from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config.from_mapping(
        DEBUG = True,
        SECRETE_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///inventario.db"
    )


    app.config['SECRET_KEY'] = 'dev'


    db.init_app(app)


    from .auth import auth_bp
    from .main import main_bp


    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)


    with app.app_context():
        db.create_all()


    return app