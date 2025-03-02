from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy 엔진 생성 (Transaction Pooler URL 사용)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)