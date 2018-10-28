import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret_key'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'PROJECT_PRODUCTION_DATABASE_URI'
    )


class DevelopmentConfig(Config):
    # DEBUG = True
    # print(os.environ.get(        'PROJECT_DEVELOPMENT_DATABASE_URI'    ))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:p@ssw0rd123@db_mysql/hacktober18'
    # SQLALCHEMY_DATABASE_URI = os.environ.get(        'PROJECT_DEVELOPMENT_DATABASE_URI'    )
    #For mysql 
    # mysql://username:password@localhost/db_name


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'PROJECT_TESTING_DATABASE_URI'
    )


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': ProductionConfig
}
