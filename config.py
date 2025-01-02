import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration"""
    # Basic Flask Config
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-lichviet')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///lichviet.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Server Config
    HOST = os.getenv('FLASK_HOST', '0.0.0.0')
    PORT = int(os.getenv('FLASK_PORT', 8088))
    
    # Application Config
    TIMEZONE = 'Asia/Ho_Chi_Minh'
    DEFAULT_LANGUAGE = 'vi'

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SQLALCHEMY_ECHO = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}