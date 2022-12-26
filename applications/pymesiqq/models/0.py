from gluon.storage import Storage
settings = Storage()

settings.migrate = True
settings.title = 'ICCI'
settings.subtitle = 'Pymes UNAP'
settings.author = 'G7'
settings.author_email = 'goyanader@estudiantesunap.cl'
settings.keywords = 'pymes unap icci'
settings.description = 'Blog para promocionar tus emprendimientos dentro de la universidad'
settings.layout_theme = 'Default'
settings.database_uri = 'sqlite://storage.sqlite'
settings.security_key = '3d37faac-1fd0-4bfa-850c-9685cf085000'
settings.email_server = 'localhost'
settings.email_sender = 'goyanader@estudiantesunap.cl'
settings.email_login = 'goyanader@estudiantesunap.cl'
settings.login_method = 'local'
settings.login_config = None
settings.plugins = []
