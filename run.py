from app import create_app, db
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app(os.getenv('FLASK_ENV', 'default'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config.get('DEBUG', False)
    )