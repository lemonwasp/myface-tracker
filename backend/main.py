import uuid
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from backend.database import SessionLocal, engine
from backend.models import Base
from backend import crud
from backend.schemas import (
    UserCreate, EmotionCreate, ActivityTypeCreate, ActivityCreate, FlowCurveCreate
)
from backend.utils.emotion_processing import process_emotion_text  # NLP 처리 함수 임포트

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 테이블 생성
Base.metadata.create_all(bind=engine)

# DB 세션 의존성
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "MyFace Tracker with Supabase & SQLAlchemy"}

# 사용자 추가
@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user.name, user.email)

# 모든 사용자 조회
@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

# 감정 추가 (선택 감정 or 자유 감정 처리 포함)
@app.post("/emotions/")
def add_emotion(emotion_data: EmotionCreate, db: Session = Depends(get_db)):
    if emotion_data.free_text:
        # 자유 감정 텍스트 입력 시 NLP 처리
        processed = process_emotion_text(emotion_data.free_text)
        emotion = processed['final_emotion']
        score = processed['emotion_score']
        keywords = ",".join(processed['keywords'])
    else:
        # 선택 감정만 입력된 경우
        emotion = emotion_data.emotion
        score = None
        keywords = None

    return crud.create_emotion(db, uuid.UUID(emotion_data.user_id), emotion, score, keywords)

# 활동 유형 추가
@app.post("/activity-types/")
def add_activity_type(activity_type: ActivityTypeCreate, db: Session = Depends(get_db)):
    return crud.create_activity_type(db, activity_type.name)

# 활동 기록 추가
@app.post("/activities/")
def add_activity(activity: ActivityCreate, db: Session = Depends(get_db)):
    return crud.create_activity(
        db,
        uuid.UUID(activity.user_id),
        uuid.UUID(activity.activity_type_id),
        activity.description
    )

# 플로우 커브 데이터 추가
@app.post("/flow-curve/")
def add_flow_curve(flow_curve: FlowCurveCreate, db: Session = Depends(get_db)):
    return crud.create_flow_curve(
        db,
        uuid.UUID(flow_curve.user_id),
        flow_curve.time_spent,
        flow_curve.satisfaction
    )