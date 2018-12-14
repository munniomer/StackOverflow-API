"""app configuration """
import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    TESTING = False
    SECRET = os.getenv('SECRET')


class Development(Config):
    """Configurations for Development."""
    DEBUG = True
    TESTING = True


class Testing(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    DEBUG = True


class Production(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


app_config = {
    "development": Development,
    "testing": Testing,
    "production": Production
}
