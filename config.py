import os
from datetime import timedelta
from dotenv import load_dotenv

# Get base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Load environment variables
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """Base config."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-lichviet')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 
        'sqlite:///' + os.path.join(basedir, 'lichviet.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    PORT = int(os.getenv('FLASK_PORT', 8088))

class DevelopmentConfig(Config):
    """Development config."""
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Production config."""
    DEBUG = False
    TESTING = False

class TestingConfig(Config):
    """Testing config."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

# Config dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}