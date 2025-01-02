from flask import render_template, redirect, url_for, request, jsonify
from datetime import datetime, timedelta
from calendar import monthcalendar
from . import main
from app.models import Event, Category
from app import db

@main.route('/')
def index():
    return redirect(url_for('main.month_view'))

@main.route('/calendar/month/<int:year>/<int:month>')
def month_view(year=None, month=None):
    if year is None or month is None:
        today = datetime.now()
        year = today.year
        month = today.month
    
    # Get calendar data
    cal = monthcalendar(year, month)
    events = Event.get_month_events(year, month)
    
    return render_template('calendar/month.html',
                         year=year,
                         month=month,
                         calendar_data=cal,
                         events=events)

@main.route('/calendar/day/<date>')
def day_view(date=None):
    if date is None:
        date = datetime.now().date()
    else:
        date = datetime.strptime(date, '%Y-%m-%d').date()
    
    events = Event.get_day_events(date)
    prev_day = date - timedelta(days=1)
    next_day = date + timedelta(days=1)
    
    return render_template('calendar/day.html',
                         date=date,
                         events=events,
                         prev_day=prev_day,
                         next_day=next_day)

@main.route('/calendar/year/<int:year>')
def year_view(year=None):
    if year is None:
        year = datetime.now().year
    
    calendar_data = {}
    for month in range(1, 13):
        calendar_data[month] = monthcalendar(year, month)
    
    return render_template('calendar/year.html',
                         year=year,
                         calendar_data=calendar_data)

# API endpoints for AJAX calls
@main.route('/api/events/<int:event_id>')
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    return jsonify(event.to_dict())

@main.route('/api/events', methods=['POST'])
def create_event():
    data = request.get_json()
    event = Event(
        title=data['title'],
        description=data.get('description', ''),
        start_time=datetime.fromisoformat(data['start_time']),
        end_time=datetime.fromisoformat(data['end_time']),
        category_id=data.get('category_id')
    )
    db.session.add(event)
    db.session.commit()
    return jsonify(event.to_dict()), 201