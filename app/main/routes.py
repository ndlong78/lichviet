from flask import render_template, redirect, url_for
from datetime import datetime
from calendar import monthcalendar
from app.main import bp
from app.models import Event
from app.utils.date_utils import get_vietnamese_month_name, get_lunar_date
from app.utils.lunar_solar_converter import converter

@bp.context_processor
def inject_functions():
    return {
        'get_lunar_date': get_lunar_date,
        'get_lunar_festival': converter.get_lunar_festival,
        'get_can_chi': converter.get_can_chi
    }

@bp.route('/calendar/month/<int:year>/<int:month>')
def month_view(year=None, month=None):
    if year is None or month is None:
        today = datetime.now()
        year = today.year
        month = today.month

    # Tính toán tháng trước và tháng sau
    prev_month = (year - 1, 12) if month == 1 else (year, month - 1)
    next_month = (year + 1, 1) if month == 12 else (year, month + 1)

    calendar_data = monthcalendar(year, month)
    events = Event.query.filter_by(year=year, month=month).all()

    return render_template('calendar/month.html',
                         year=year,
                         month=month,
                         month_name=get_vietnamese_month_name(month),
                         calendar_data=calendar_data,
                         events=events,
                         prev_month=prev_month,
                         next_month=next_month)