from flask import Blueprint

bp = Blueprint('api', __name__)

# Import các routes API
from app.api import events, categories