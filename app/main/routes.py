from flask import render_template, redirect, url_for
from datetime import datetime
from app.main import main  # Import blueprint main từ package hiện tại
from app.models import Event, Category
from app import db

@main.route('/')
def index():
    return render_template('index.html')

# Thêm các routes khác...