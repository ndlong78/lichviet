import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    # Ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # Register the datetime filter
    def datetime_filter(value, format='%Y-%m-%d %H:%M:%S', *args, **kwargs):
        if isinstance(value, datetime):
            return value.strftime(format)
        return value
    
    app.jinja_env.filters['datetime'] = datetime_filter

    # Register the filter_events_by_date filter
    def filter_events_by_date(events, day, month, year):
        start_date = datetime(year, month, day)
        end_date = datetime(year, month, day + 1)
        return [event for event in events if start_date <= event.start_time < end_date]
    
    app.jinja_env.filters['filter_events_by_date'] = filter_events_by_date
    
    return app

from app import models