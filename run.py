from flask import Flask
from routes_auth import auth_bp
from routes_report import report_bp
from routes_notify import notify_bp
from database import init_db

app = Flask(__name__)
app.config.from_object("config")

# JWT secret 설정 (환경변수 사용 가능)
app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']

# DB 초기화
init_db(app)

# 블루프린트 등록
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(report_bp, url_prefix="/api/report")
app.register_blueprint(notify_bp, url_prefix="/api/notify")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
