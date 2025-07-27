from flask import Flask
from routes_auth import auth_bp
from routes_report import report_bp
from routes_notify import notify_bp
from database import init_db, db
from config import *
from models_user import User
from models_event import Event

app = Flask(__name__)

# 🔧 환경변수 및 Firebase 초기화 포함된 config.py 로드
app.config.from_object("config")

# 🔐 JWT 시크릿키 설정
app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']

# 🗄️ DB 초기화 (Render의 DATABASE_URL 환경변수 사용)
init_db(app)

# ✅ 서버 실행 시 테이블 자동 생성 (Shell 필요 없음)
with app.app_context():
    db.create_all()

# 📦 라우트 등록
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(report_bp, url_prefix="/api/report")
app.register_blueprint(notify_bp, url_prefix="/api/notify")

# ▶️ 앱 실행
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
