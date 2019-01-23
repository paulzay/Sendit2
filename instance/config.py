import os

class BaseConfig:
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    ENV = 'development'
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    ENV = 'testing'
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    ENV = 'production'
    DEBUG = False
    TESTING = False

app_config = dict(
    development = DevelopmentConfig,
    testing = TestingConfig,
    production = ProductionConfig
)