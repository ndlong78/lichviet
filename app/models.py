from datetime import datetime
from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def get_month_events(year, month):
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1)
        else:
            end_date = datetime(year, month + 1, 1)
        return Event.query.filter(
            Event.start_time >= start_date,
            Event.start_time < end_date
        ).all()

    @staticmethod
    def get_day_events(date):
        return Event.query.filter(
            db.func.date(Event.start_time) == date.date()
        ).all()

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), default="#3498db")
    events = db.relationship('Event', backref='category', lazy=True)