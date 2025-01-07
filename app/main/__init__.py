from flask import Blueprint

bp = Blueprint('main', __name__)

# Import routes sau khi tạo blueprint
from app.main import routes