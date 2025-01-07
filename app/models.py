from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
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

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    events = db.relationship('Event', backref='user', lazy='dynamic')
    categories = db.relationship('Category', backref='user', lazy='dynamic')

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise ValueError('Email không được để trống')
        if '@' not in email:
            raise ValueError('Email không hợp lệ')
        return email

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError('Username không được để trống')
        if len(username) < 3:
            raise ValueError('Username phải có ít nhất 3 ký tự')
        return username

    def set_password(self, password):
        if len(password) < 6:
            raise ValueError('Mật khẩu phải có ít nhất 6 ký tự')
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(200))
    is_lunar = db.Column(db.Boolean, default=False)
    is_all_day = db.Column(db.Boolean, default=False)
    
    # Repeat settings
    repeat_type = db.Column(db.Enum(RepeatType), default=RepeatType.NONE)
    repeat_end_date = db.Column(db.DateTime)
    repeat_interval = db.Column(db.Integer, default=1)  # For example, every 2 weeks
    
    # Reminders
    reminder_minutes = db.Column(db.Integer)  # Minutes before event to remind
    
    # Foreign keys
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    category = db.relationship('Category', backref='events')

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError('Tiêu đề không được để trống')
        if len(title) > 100:
            raise ValueError('Tiêu đề không được quá 100 ký tự')
        return title

    @validates('start_time', 'end_time')
    def validate_times(self, key, time):
        if not time:
            raise ValueError(f'{key} không được để trống')
        if key == 'end_time' and hasattr(self, 'start_time') and self.start_time:
            if time < self.start_time:
                raise ValueError('Thời gian kết thúc phải sau thời gian bắt đầu')
        return time

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'start_time': self.start_time.isoformat(),
            'end_time': self.end_time.isoformat(),
            'location': self.location,
            'is_lunar': self.is_lunar,
            'is_all_day': self.is_all_day,
            'repeat_type': self.repeat_type.value if self.repeat_type else 'none',
            'repeat_end_date': self.repeat_end_date.isoformat() if self.repeat_end_date else None,
            'repeat_interval': self.repeat_interval,
            'reminder_minutes': self.reminder_minutes,
            'category': self.category.to_dict() if self.category else None,
            'user_id': self.user_id
        }

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), default='#3498db')
    description = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError('Tên danh mục không được để trống')
        if len(name) > 50:
            raise ValueError('Tên danh mục không được quá 50 ký tự')
        return name

    @validates('color')
    def validate_color(self, key, color):
        if not color:
            return '#3498db'  # Default color
        if not color.startswith('#') or len(color) != 7:
            raise ValueError('Mã màu không hợp lệ (format: #RRGGBB)')
        return color

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            'description': self.description,
            'user_id': self.user_id
        }