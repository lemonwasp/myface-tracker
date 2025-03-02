# DB 연결 테스트만 하는 파일

from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        print("✅ DB 연결 성공")
except Exception as e:
    print(f"❌ DB 연결 실패: {e}")
