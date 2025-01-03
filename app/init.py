from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Register blueprints
        from app.main import bp as main_bp
        app.register_blueprint(main_bp)

        # Create database tables
        db.create_all()

    return app

from app import models