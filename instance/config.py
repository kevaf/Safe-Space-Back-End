import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'thisiskev'
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://moringa:kev2214@localhost/safespace"


class DevelopmentConfig(Config):
    """Configurations for Development."""
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_GB")


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/test_db'
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}