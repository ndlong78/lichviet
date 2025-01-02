from flask import Blueprint

# Tạo blueprint trước khi import routes
main = Blueprint('main', __name__)

# Import routes sau khi tạo blueprint
from app.main import routes