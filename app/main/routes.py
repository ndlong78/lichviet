from flask import render_template, redirect, url_for, request
from datetime import datetime, timedelta
from calendar import monthcalendar
from app.main import bp
from app.models import Event, Category
from app.utils.date_utils import get_vietnamese_month_name, get_lunar_date

# Define the is_today function
def is_today(day, month, year):
    today = datetime.today()
    return today.year == year and today.month == month and today.day == day

# Context processor to inject functions into Jinja2 templates
@bp.app_context_processor
def inject_functions():
    return dict(get_lunar_date=get_lunar_date)

@bp.route('/')
def index():
    """Home page"""
    return redirect(url_for('main.calendar'))

@bp.route('/calendar')
def calendar():
    """Default calendar view - redirect to the current month view"""
    today = datetime.now()
    return redirect(url_for('main.month_view', 
                          year=today.year, 
                          month=today.month))

@bp.route('/calendar/month')
@bp.route('/calendar/month/<int:year>/<int:month>')
def month_view(year=None, month=None):
    """Display calendar by month"""
    if year is None or month is None:
        today = datetime.now()
        year = today.year
        month = today.month

    # Calculate the previous and next months
    if month == 1:
        prev_month = (year - 1, 12)
    else:
        prev_month = (year, month - 1)
        
    if month == 12:
        next_month = (year + 1, 1)
    else:
        next_month = (year, month + 1)

    # Get calendar data
    calendar_data = monthcalendar(year, month)
    
    # Get events in the month
    events = Event.get_month_events(year, month)

    # Convert day to datetime object
    for week in calendar_data:
        for i in range(len(week)):
            if week[i] != 0:
                week[i] = datetime(year, month, week[i])

    return render_template('calendar/month.html',
                         year=year,
                         month=month,
                         month_name=get_vietnamese_month_name(month),
                         calendar_data=calendar_data,
                         events=events,
                         prev_month=prev_month,
                         next_month=next_month,
                         is_today=is_today)

@bp.route('/calendar/week')
@bp.route('/calendar/week/<int:year>/<int:week>')
def week_view(year=None, week=None):
    """Display calendar by week"""
    if year is None or week is None:
        today = datetime.now()
        year = today.year
        week = today.isocalendar()[1]

    return render_template('calendar/week.html',
                         year=year,
                         week=week)

@bp.route('/calendar/day')
@bp.route('/calendar/day/<int:year>/<int:month>/<int:day>')
def day_view(year=None, month=None, day=None):
    """Display calendar by day"""
    if year is None or month is None or day is None:
        today = datetime.now()
        year = today.year
        month = today.month
        day = today.day

    current_date = datetime(year, month, day)
    events = Event.get_day_events(current_date)

    return render_template('calendar/day.html',
                         current_date=current_date,
                         events=events)

@bp.route('/calendar/year')
@bp.route('/calendar/year/<int:year>')
def year_view(year=None):
    """Display calendar by year"""
    if year is None:
        year = datetime.now().year

    months_data = {}
    for month in range(1, 13):
        months_data[month] = monthcalendar(year, month)

    return render_template('calendar/year.html',
                         year=year,
                         months_data=months_data)