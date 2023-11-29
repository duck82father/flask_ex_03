from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy # SQLAlchemy (파이썬 ORM 라이브러리)
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, auth_views, question_views, hobby_views # answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(hobby_views.bp)
    # app.register_blueprint(answer_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app