from flask import render_template, redirect, url_for, request
from app.main import main
from app import db
from app.models import Event, Category, Tag

@main.route('/')
def index():
    return render_template('index.html')