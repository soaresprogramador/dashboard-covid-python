import os


class Config:
    CSRF_ENABLE = True
    # Base para criacao de senhas
    SECRET = '@1234#4321@'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
    APP = None


class DevelopmentConfig(Config):
    DEBUG = True
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)  # http://localhost:8000
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://tiago.silva2:de_m7jBG^WZ=@localhost:3306/dashboard_aula'


app_config = {
    'development': DevelopmentConfig(),
    'testing': None
}


app_active = os.getenv('FLASK_ENV')
if app_active is None:
    app_active = 'development'

# class TestingConfig(Config):
    # DEBUG = False
    # TESTING = True
    # IP_HOST = '192.0.0.1'
    # PORT_HOST = 8080
    # URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)  # http://localhost:8000
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://tiago.silva2:de_m7jBG^WZ=@192.0.0.1:3306/dashboard_prof'


# class ProductionConfig(Config):
    # DEBUG = False
    # TESTING = False
    # IP_HOST = '192.0.5.1'
    # PORT_HOST = 8080
    # URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)  # http://localhost:8000
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://tiago.silva2:de_m7jBG^WZ=@192.0.0.1:3306/dashboard_prof'
