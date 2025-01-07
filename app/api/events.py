from flask import jsonify, request
from app.api import bp
from app.models import Event, db

@bp.route('/events', methods=['GET'])
def get_events():
    """API endpoint để lấy danh sách sự kiện"""
    events = Event.query.all()
    return jsonify([event.to_dict() for event in events])

@bp.route('/events', methods=['POST'])
def create_event():
    """API endpoint để tạo sự kiện mới"""
    data = request.get_json()
    event = Event()
    event.from_dict(data)
    db.session.add(event)
    db.session.commit()
    return jsonify(event.to_dict()), 201