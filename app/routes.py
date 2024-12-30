from flask import render_template
from app import app
from app.models import Event
from datetime import datetime, timedelta

@app.route('/')
def home():
    events = Event.query.all()
    return render_template('index.html', events=events)

@app.route('/day/<date>')
def day_view(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    events = Event.query.filter_by(date=date_obj).all()
    return render_template('day.html', events=events, date=date_obj)

@app.route('/week/<date>')
def week_view(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    start_week = date_obj - timedelta(days=date_obj.weekday())
    end_week = start_week + timedelta(days=6)
    events = Event.query.filter(Event.date.between(start_week, end_week)).all()
    return render_template('week.html', events=events, start_week=start_week, end_week=end_week)

@app.route('/month/<year>/<month>')
def month_view(year, month):
    events = Event.query.filter(db.extract('year', Event.date) == year, db.extract('month', Event.date) == month).all()
    return render_template('month.html', events=events, year=year, month=month)

@app.route('/year/<year>')
def year_view(year):
    events = Event.query.filter(db.extract('year', Event.date) == year).all()
    return render_template('year.html', events=events, year=year)

@app.route('/about')
def about():
    return render_template('about.html')