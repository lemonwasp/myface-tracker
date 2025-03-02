# Pydantic 추가(입력 데이터 검증용)

from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str

class EmotionCreate(BaseModel):
    user_id: str
    emotion: Optional[str] = None  # 선택 감정 (happy, sad 등)
    free_text: Optional[str] = None  # 자유 감정 입력

class ActivityTypeCreate(BaseModel):
    name: str

class ActivityCreate(BaseModel):
    user_id: str
    activity_type_id: str
    description: str

class FlowCurveCreate(BaseModel):
    user_id: str
    time_spent: float
    satisfaction: float