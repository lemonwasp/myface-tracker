import requests

base_url = "http://127.0.0.1:8000"

def check_response(res):
    try:
        print(res.status_code, res.json())
    except requests.exceptions.JSONDecodeError:
        print(f"응답 파싱 실패: {res.status_code} {res.text}")

# 사용자 추가 (UUID 기반)
res = requests.post(f"{base_url}/users/", json={"name": "홍태관", "email": "htg@example.com"})
check_response(res)

# 사용자 추가가 성공하면, 사용자 ID(UUID)를 저장
if res.status_code == 200:
    user_id = res.json()["id"]
else:
    raise Exception("User creation failed")

# 활동 유형 추가
res = requests.post(f"{base_url}/activity-types/", json={"name": "운동"})
check_response(res)

# 활동 유형 추가 성공 시 활동 타입 ID 저장
if res.status_code == 200:
    activity_type_id = res.json()["id"]
else:
    raise Exception("Activity type creation failed")

# 감정 추가
res = requests.post(f"{base_url}/emotions/", json={"user_id": user_id, "emotion": "happy"})
check_response(res)

# 활동 추가
res = requests.post(f"{base_url}/activities/", json={
    "user_id": user_id,
    "activity_type_id": activity_type_id,
    "description": "아침 조깅"
})
check_response(res)

# 플로우 커브 추가
res = requests.post(f"{base_url}/flow-curve/", json={
    "user_id": user_id,
    "time_spent": 1.5,
    "satisfaction": 4.5
})
check_response(res)

# 사용자 목록 조회
res = requests.get(f"{base_url}/users/")
check_response(res)