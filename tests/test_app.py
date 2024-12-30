# tests/test_app.py
import pytest
from app import app, db
from app.models import Event

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_event_creation(client):
    new_event = Event(date='2023-01-01', description='New Year')
    db.session.add(new_event)
    db.session.commit()
    assert new_event in db.session