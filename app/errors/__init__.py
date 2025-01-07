from flask import Blueprint

bp = Blueprint('errors', __name__)

# Import các handlers
from app.errors import handlers