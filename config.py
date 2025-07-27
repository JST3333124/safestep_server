import os

# Firebase 인증 키 파일 경로
FCM_CREDENTIALS = "firebase-adminsdk.json"

# 데이터베이스 URL (환경변수가 없으면 SQLite 기본 파일로)
DATABASE_URL = os.environ.get("DATABASE_URL")

# JWT용 시크릿 키 (없으면 디폴트로 설정)
SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-key")
