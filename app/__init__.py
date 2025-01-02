from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import và đăng ký blueprint
    with app.app_context():
        # Import blueprint ở đây để tránh circular import
        from app.main import main as main_blueprint
        app.register_blueprint(main_blueprint)
    
    return app