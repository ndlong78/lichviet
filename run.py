from app import create_app
from dotenv import load_dotenv
import os

load_dotenv()

app = create_app(os.getenv('FLASK_ENV', 'development'))

if __name__ == '__main__':
    app.run(
        host=os.getenv('FLASK_HOST', '0.0.0.0'),
        port=int(os.getenv('FLASK_PORT', 8088)),
        debug=os.getenv('FLASK_DEBUG', True)
    )