# 각 테이블에 데이터 추가, 조회 등 로직(DB 접근 함수)

from sqlalchemy.orm import Session
from backend.models import User, Emotion, Activity, ActivityType, FlowCurve
import uuid

# 사용자 생성 (이메일 중복 체크 포함)
def create_user(db: Session, name: str, email: str):
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        return existing_user  # 이미 있으면 그대로 반환
    db_user = User(id=uuid.uuid4(), name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 모든 사용자 조회
def get_users(db: Session):
    return db.query(User).all()

# 감정 기록 추가
def create_emotion(db: Session, user_id: uuid.UUID, emotion: str):
    db_emotion = Emotion(user_id=user_id, emotion=emotion)
    db.add(db_emotion)
    db.commit()
    db.refresh(db_emotion)  # 여기 원래 오류 있었음
    return db_emotion

# 활동 유형 추가 (중복 체크 추가)
def create_activity_type(db: Session, name: str):
    existing_type = db.query(ActivityType).filter(ActivityType.name == name).first()
    if existing_type:
        return existing_type  # 이미 있으면 기존거 반환
    db_activity_type = ActivityType(name=name)
    db.add(db_activity_type)
    db.commit()
    db.refresh(db_activity_type)
    return db_activity_type

# 활동 기록 추가
def create_activity(db: Session, user_id: uuid.UUID, activity_type_id: int, description: str):
    db_activity = Activity(user_id=user_id, activity_type_id=activity_type_id, description=description)
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity

# 플로우 커브 데이터 추가
def create_flow_curve(db: Session, user_id: uuid.UUID, time_spent: float, satisfaction: float):
    db_flow_curve = FlowCurve(user_id=user_id, time_spent=time_spent, satisfaction=satisfaction)
    db.add(db_flow_curve)
    db.commit()
    db.refresh(db_flow_curve)
    return db_flow_curve