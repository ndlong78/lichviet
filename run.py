#!/usr/bin/env python3
from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app(os.getenv('FLASK_ENV', 'default'))

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config.get('DEBUG', False)
    )