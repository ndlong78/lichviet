from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config

# Khởi tạo các extension
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name='default'):
    """
    Application Factory Function
    """
    app = Flask(__name__)
    
    # Load config
    app.config.from_object(config[config_name])
    
    # Khởi tạo database
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import và đăng ký các blueprint
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Tạo tables khi khởi động ứng dụng
    with app.app_context():
        db.create_all()
        initialize_database()
        
    return app

def initialize_database():
    """
    Khởi tạo dữ liệu mặc định cho database
    """
    from app.models import Category, Tag, UserPreference
    
    # Kiểm tra xem database đã có dữ liệu chưa
    if Category.query.first() is None:
        # Tạo categories mặc định
        default_categories = [
            {'name': 'Công việc', 'color': '#e74c3c', 'description': 'Các sự kiện liên quan đến công việc'},
            {'name': 'Cá nhân', 'color': '#3498db', 'description': 'Các sự kiện cá nhân'},
            {'name': 'Gia đình', 'color': '#2ecc71', 'description': 'Các sự kiện gia đình'},
            {'name': 'Học tập', 'color': '#f1c40f', 'description': 'Các sự kiện học tập'},
            {'name': 'Nghỉ lễ', 'color': '#9b59b6', 'description': 'Các ngày nghỉ lễ'},
        ]
        
        for cat in default_categories:
            category = Category(
                name=cat['name'],
                color=cat['color'],
                description=cat['description']
            )
            db.session.add(category)
    
    if Tag.query.first() is None:
        # Tạo tags mặc định
        default_tags = [
            'Quan trọng', 'Gấp', 'Cuộc họp', 'Du lịch', 
            'Sinh nhật', 'Deadline', 'Sức khỏe', 'Giải trí'
        ]
        
        for tag_name in default_tags:
            tag = Tag(name=tag_name)
            db.session.add(tag)
    
    # Commit các thay đổi
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(f"Error initializing database: {str(e)}")