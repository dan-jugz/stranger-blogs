import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://daniel:watchlist@localhost/blogg'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")    

class DevConfig(Config):
        DEBUG = True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}