# _*_ Coding:utf-8 _*_
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_migrate import Migrate
# from flask_debugtoolbar import DebugToolbarExtension
db = SQLAlchemy()
migrate=Migrate()
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    # 注册蓝图
    from app.home import home as home_blueprint
    from app.admin import admin as admin_blueprint
    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint,url_prefix="/admin")
    return app




