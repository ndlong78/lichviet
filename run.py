import os
from app import create_app
from config import config

# Lấy config class từ dictionary config
app = create_app(config[os.getenv('FLASK_ENV', 'development')])

if __name__ == '__main__':
    app.run(
        host=app.config['HOST'],
        port=app.config['PORT'],
        debug=app.config.get('DEBUG', False)
    )