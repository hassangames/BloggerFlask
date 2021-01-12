import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "HARDTOGUSSS"
    DEBUG =True
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    FLASK_APP = os.getenv('FLASK_APP')
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = "halsmiri@ucas.edu.ps"
    MAIL_PASSWORD = "Hhssanpy1998!@#"
    FLASKY_MAIL_SUBJECT_PREFIX = '[HASSAN]'
    FLASKY_MAIL_SENDER = 'HASSAN Admin <halsmiri@ucas.edu.ps>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/Blogger'
    ADMIN_MAIL = 'halsmiri@ucas.edu.ps'
    @staticmethod
    def init_db():
        pass


# class DevelopmentConfig(Config):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = 'mysql://root:rootd@localhost/flaskdb'
#
#
# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
#                               'sqlite://'
#
#
# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#                               'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#
#
