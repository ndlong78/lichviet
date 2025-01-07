from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login
import pytz
from sqlalchemy.orm import validates
from enum import Enum

class RepeatType(Enum):
    NONE = 'none'
    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'
    LUNAR_MONTHLY = 'lunar_monthly'
    LUNAR_YEARLY = 'lunar_yearly'

class NotificationType(Enum):
    EMAIL = 'email'
    PUSH = 'push'
    SMS = 'sms'

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    timezone = db.Column(db.String(50), default='UTC')
    preferences = db.Column(db.JSON, default={})
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    events = db.relationship('Event', backref='user', lazy='dynamic')
    categories = db.relationship('Category', backref='user', lazy='dynamic')
    shared_calendars = db.relationship('CalendarSharing', 
                                     foreign_keys='CalendarSharing.shared_with_id',
                                     backref='shared_user')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}" if self.first_name and self.last_name else self.username

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False, index=True)
    end_time = db.Column(db.DateTime, nullable=False, index=True)
    location = db.Column(db.String(200))
    is_lunar = db.Column(db.Boolean, default=False)
    is_all_day = db.Column(db.Boolean, default=False)
    visibility = db.Column(db.Enum('public', 'private', 'shared', name='event_visibility'))
    
    # Repeat settings
    repeat_type = db.Column(db.Enum(RepeatType), default=RepeatType.NONE)
    repeat_end_date = db.Column(db.DateTime)
    repeat_interval = db.Column(db.Integer, default=1)
    
    # Additional fields
    attachments = db.Column(db.JSON, default=[])
    metadata = db.Column(db.JSON, default={})
    status = db.Column(db.String(20), default='active')
    
    # Foreign keys
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Relationships
    reminders = db.relationship('EventReminder', backref='event', cascade='all, delete-orphan')

class EventReminder(db.Model):
    __tablename__ = 'event_reminders'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    notification_type = db.Column(db.Enum(NotificationType))
    minutes_before = db.Column(db.Integer, nullable=False)
    is_sent = db.Column(db.Boolean, default=False)
    sent_at = db.Column(db.DateTime)
    
    @validates('minutes_before')
    def validate_minutes(self, key, minutes):
        if minutes <= 0:
            raise ValueError('Minutes before must be positive')
        return minutes

class CalendarSharing(db.Model):
    __tablename__ = 'calendar_sharing'
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    shared_with_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    permission = db.Column(db.Enum('read', 'write', name='share_permissions'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)