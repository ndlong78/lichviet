from flask import render_template, redirect, url_for, request, jsonify
from datetime import datetime, timedelta
from calendar import monthcalendar
from app.main import bp
from app.models import Event, Category
from app.utils.date_utils import get_vietnamese_month_name, get_lunar_date
from app.utils.lunar.converter import LunarConverter

@bp.route('/')
@bp.route('/index')
def index():
    return redirect(url_for('main.month_view'))

@bp.route('/calendar/month')
@bp.route('/calendar/month/<int:year>/<int:month>')
def month_view(year=None, month=None):
    if year is None or month is None:
        today = datetime.now()
        year = today.year
        month = today.month

    prev_month = (year - 1, 12) if month == 1 else (year, month - 1)
    next_month = (year + 1, 1) if month == 12 else (year, month + 1)

    calendar_data = monthcalendar(year, month)
    events = Event.query.filter(
        Event.start_time >= datetime(year, month, 1),
        Event.start_time < datetime(year + (month//12), ((month%12)+1), 1)
    ).all()

    return render_template('calendar/month.html',
                         year=year,
                         month=month,
                         month_name=get_vietnamese_month_name(month),
                         calendar_data=calendar_data,
                         events=events,
                         prev_month=prev_month,
                         next_month=next_month)

@bp.route('/calendar/day/<int:year>/<int:month>/<int:day>')
def day_view(year, month, day):
    current_date = datetime(year, month, day)
    events = Event.query.filter(
        Event.start_time >= current_date,
        Event.start_time < current_date + timedelta(days=1)
    ).all()
    
    return render_template('calendar/day.html',
                         current_date=current_date,
                         events=events)