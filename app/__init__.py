# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
import pytz
from datetime import datetime

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    """Application Factory"""
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Set timezone
    app.timezone = pytz.timezone(app.config['TIMEZONE'])
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Custom template filters
    @app.template_filter('localdatetime')
    def localdatetime_filter(date):
        """Convert UTC datetime to local timezone"""
        if date is None:
            return ""
        utc = pytz.UTC
        if not date.tzinfo:
            date = utc.localize(date)
        return date.astimezone(app.timezone)
    
    # Initialize database
    with app.app_context():
        db.create_all()
        initialize_database()
        
    return app

def initialize_database():
    """Initialize database with default data"""
    from app.models import Category, Tag
    
    # Only initialize if database is empty
    if not Category.query.first():
        try:
            # Add default categories and tags
            from app.default_data import create_default_data
            create_default_data()
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Error initializing database: {str(e)}")