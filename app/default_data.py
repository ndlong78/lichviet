# app/default_data.py
from app.models import Category, Tag
from app import db

def create_default_data():
    """Create default categories and tags"""
    # Default categories
    categories = [
        {'name': 'Công việc', 'color': '#e74c3c', 'description': 'Các sự kiện công việc'},
        {'name': 'Cá nhân', 'color': '#3498db', 'description': 'Các sự kiện cá nhân'},
        {'name': 'Gia đình', 'color': '#2ecc71', 'description': 'Các sự kiện gia đình'},
        {'name': 'Học tập', 'color': '#f1c40f', 'description': 'Các sự kiện học tập'},
        {'name': 'Nghỉ lễ', 'color': '#9b59b6', 'description': 'Các ngày nghỉ lễ'},
    ]
    
    # Default tags
    tags = [
        'Quan trọng', 'Gấp', 'Cuộc họp', 'Du lịch',
        'Sinh nhật', 'Deadline', 'Sức khỏe', 'Giải trí'
    ]
    
    # Add categories
    for cat_data in categories:
        category = Category(**cat_data)
        db.session.add(category)
    
    # Add tags
    for tag_name in tags:
        tag = Tag(name=tag_name)
        db.session.add(tag)