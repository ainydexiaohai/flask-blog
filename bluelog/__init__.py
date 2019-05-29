from flask import Flask
from bluelog.blueprints import blog_bp, admin_bp, auth_bp
from bluelog.settings import config
from bluelog.extensions import ckeditor,bootstrap,db,mail,moment
import os


def create_app(config_name = None):
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    app = Flask('bluelog')
    app.config.from_object(config[config_name])
    app.register_blueprint(blog_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(auth_bp)

    ckeditor.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    moment.init_app(app)

    return app
