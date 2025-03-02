# 테이블 구조 및 설정

import uuid
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# 사용자 테이블 (users)
class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

# 감정 테이블 (emotions)
class Emotion(Base):
    __tablename__ = "emotions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    emotion = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# 활동 유형 테이블 (activity_types)
class ActivityType(Base):
    __tablename__ = "activity_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

# 활동 기록 테이블 (activities)
class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    activity_type_id = Column(Integer, ForeignKey("activity_types.id"))
    description = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# 플로우 커브 데이터 (flow_curve)
class FlowCurve(Base):
    __tablename__ = "flow_curve"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    time_spent = Column(Float)
    satisfaction = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
