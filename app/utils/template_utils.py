from datetime import datetime
from app import app
from .lunar_calendar import solar_to_lunar

def register_template_utils(app):
    @app.template_filter('format_date')
    def format_date(date, format='%d/%m/%Y'):
        return date.strftime(format)

    @app.context_processor
    def utility_processor():
        return {
            'now': datetime.now,
            'get_lunar_date': solar_to_lunar
        }