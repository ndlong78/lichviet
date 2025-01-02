from app import db
from datetime import datetime

# Association table for Event-Tag many-to-many relationship
event_tags = db.Table('event_tag',
    db.Column('event_id', db.Integer, db.ForeignKey('event.id', ondelete='CASCADE'), primary_key=True),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id', ondelete='CASCADE'), primary_key=True)
)

class Event(db.Model):
    """Model cho các sự kiện trong lịch"""
    __tablename__ = 'event'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False, index=True)
    time = db.Column(db.Time, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=True)
    is_important = db.Column(db.Boolean, default=False)
    repeat_type = db.Column(db.String(20), nullable=True)
    color = db.Column(db.String(7), default="#3498db")
    created_by = db.Column(db.String(100), nullable=True)

    # Relationships
    category = db.relationship('Category', backref='events')
    reminders = db.relationship('Reminder', backref='event', cascade='all, delete-orphan')
    tags = db.relationship('Tag', secondary=event_tags, backref=db.backref('events', lazy='dynamic'))

class Category(db.Model):
    """Model cho các danh mục sự kiện"""
    __tablename__ = 'category'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    color = db.Column(db.String(7), default="#3498db")
    description = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Tag(db.Model):
    """Model cho các tag"""
    __tablename__ = 'tag'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Reminder(db.Model):
    """Model cho các nhắc nhở"""
    __tablename__ = 'reminder'
    
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id', ondelete='CASCADE'), nullable=False)
    reminder_time = db.Column(db.DateTime, nullable=False)
    is_sent = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class UserPreference(db.Model):
    """Model cho cài đặt người dùng"""
    __tablename__ = 'user_preference'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), unique=True, nullable=False)
    default_view = db.Column(db.String(10), default='month')
    theme = db.Column(db.String(20), default='light')
    start_day = db.Column(db.Integer, default=0)
    show_weekends = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)