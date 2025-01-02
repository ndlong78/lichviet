from config import config
app.config.from_object(config[os.getenv('FLASK_ENV', 'default')])