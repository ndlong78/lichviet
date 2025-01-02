from app import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), nullable=False, default='#3498db')
    description = db.Column(db.String(200))
    
    events = db.relationship('Event', backref='category', lazy=True)
    
    def __repr__(self):
        return f'<Category {self.name}>'

class Event(db.Model):
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, 
                          onupdate=datetime.utcnow)
    
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    
    def __repr__(self):
        return f'<Event {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'location': self.location,
            'category': self.category.name if self.category else None,
            'category_color': self.category.color if self.category else None
        }
    
    @staticmethod
    def get_day_events(date):
        return Event.query.filter(
            db.func.date(Event.start_time) == date
        ).order_by(Event.start_time).all()
    
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
        ).order_by(Event.start_time).all()