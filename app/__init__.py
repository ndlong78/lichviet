from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
cache = Cache()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Thêm cấu hình này nếu chưa có
    app.config['CACHE_TYPE'] = 'simple'  # Sử dụng cấu hình cache đơn giản

    db.init_app(app)
    cache.init_app(app)

    with app.app_context():
        # Import parts of our application
        from app.main import routes  # Thực hiện import sau khi khởi tạo app
        db.create_all()

    return app