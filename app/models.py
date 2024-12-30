from app import db

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Event {self.date} - {self.description}>'