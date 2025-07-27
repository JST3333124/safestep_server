from flask_sqlalchemy import SQLAlchemy

# Flask 앱이 전달되기 전까지는 전역 인스턴스만 정의
db = SQLAlchemy()

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["DATABASE_URL"]
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    with app.app_context():
        from models_user import User
        from models_event import Event
        db.create_all()
