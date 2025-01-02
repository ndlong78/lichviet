# run.py
import os
from app import create_app, db
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create app instance
app = create_app(os.getenv('FLASK_ENV', 'default'))

def main():
    """Main entry point"""
    with app.app_context():
        db.create_all()
    
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config['DEBUG']
    )

if __name__ == '__main__':
    main()