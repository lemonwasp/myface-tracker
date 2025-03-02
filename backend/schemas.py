# Pydantic추가(입력 데이터 검증용)

from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class EmotionCreate(BaseModel):
    user_id: str
    emotion: str

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
