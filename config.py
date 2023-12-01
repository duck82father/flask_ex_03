import os

BASE_DIR = os.path.dirname(__file__)

# 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'svm_model.db'))

# SQLAlchemy의 이벤트를 처리하는 옵션
SQLALCHEMY_TRACK_MODIFICATIONS = False


# 파일 업로드 처리
UPLOAD_FORDER = "uploads/"
MAX_CONTENT_LENGTH = 16*1024*1024 # 최대 16MB 파일 허용

SECRET_KEY = "dev"
