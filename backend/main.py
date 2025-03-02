from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import uuid
from .database import get_db_connection, init_db

app = FastAPI()

# 앱 시작 시 DB 초기화
@app.on_event("startup")
def startup():
    init_db()

# 요청 데이터 구조 정의
class RecordCreate(BaseModel):
    user_id: str
    activity_name: str
    emotion: str
    flow_score: int
    memo: str

# 기록 저장 API
@app.post("/records")
async def create_record(record: RecordCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    record_id = str(uuid.uuid4())
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("""
    INSERT INTO activities (record_id, user_id, activity_name, emotion, flow_score, timestamp, memo)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (record_id, record.user_id, record.activity_name, record.emotion, record.flow_score, timestamp, record.memo))
    
    conn.commit()
    conn.close()
    
    return {"record_id": record_id, "message": "기록 저장 완료"}