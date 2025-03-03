# 각 테이블에 데이터 추가, 조회 등 로직(DB 접근 함수)

from sqlalchemy.orm import Session
from backend.models import User, Emotion, Activity, ActivityType, FlowCurve
import uuid
from typing import Optional

# 사용자 생성
def create_user(db: Session, name: str, email: str):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        return {"error": "이미 존재하는 이메일입니다."}

    db_user = User(id=uuid.uuid4(), name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 모든 사용자 조회
def get_users(db: Session):
    return db.query(User).all()

# 감정 기록 추가 (선택 감정 or NLP 분석 결과 포함 감정)
def create_emotion(db: Session, user_id: uuid.UUID, emotion: str, emotion_score: Optional[float], keywords: Optional[str]):
    db_emotion = Emotion(
        id=uuid.uuid4(),
        user_id=user_id,
        emotion=emotion,
        emotion_score=emotion_score,
        emotion_keywords=keywords,
    )
    db.add(db_emotion)
    db.commit()
    db.refresh(db_emotion)
    return db_emotion

# 활동 유형 추가
def create_activity_type(db: Session, name: str):
    db_activity_type = ActivityType(id=uuid.uuid4(), name=name)
    db.add(db_activity_type)
    db.commit()
    db.refresh(db_activity_type)
    return db_activity_type

# 활동 기록 추가
def create_activity(db: Session, user_id: uuid.UUID, activity_type_id: uuid.UUID, description: str):
    db_activity = Activity(
        id=uuid.uuid4(),
        user_id=user_id,
        activity_type_id=activity_type_id,
        description=description,
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

# 플로우 커브 데이터 추가
def create_flow_curve(db: Session, user_id: uuid.UUID, time_spent: float, satisfaction: float):
    db_flow_curve = FlowCurve(
        id=uuid.uuid4(),
        user_id=user_id,
        time_spent=time_spent,
        satisfaction=satisfaction,
    )
    db.add(db_flow_curve)
    db.commit()
    db.refresh(db_flow_curve)
    return db_flow_curve