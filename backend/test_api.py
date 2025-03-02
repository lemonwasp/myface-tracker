import requests

base_url = "http://127.0.0.1:8000"

def check_response(res):
    try:
        print(res.status_code, res.json())
    except requests.exceptions.JSONDecodeError:
        print(f"응답 파싱 실패: {res.status_code} {res.text}")


# 1. 사용자 추가 (UUID 기반)
res = requests.post(f"{base_url}/users/", json={"name": "홍태관", "email": "htg@example.com"})
check_response(res)

if res.status_code == 200:
    user_id = res.json()["id"]
else:
    raise Exception("User creation failed")

# 2. 활동 유형 추가
res = requests.post(f"{base_url}/activity-types/", json={"name": "운동"})
check_response(res)

if res.status_code == 200:
    activity_type_id = res.json()["id"]
else:
    raise Exception("Activity type creation failed")

# 3. 감정 추가 (선택 감정) - happy, sad 같은 선택형 감정
res = requests.post(f"{base_url}/emotions/", json={
    "user_id": user_id,
    "emotion": "happy"
})
check_response(res)

# 4. 감정 추가 (직접 입력 감정) - NLP 전처리 테스트용
res = requests.post(f"{base_url}/emotions/free-text", json={
    "user_id": user_id,
    "free_text": "요즘 기분이 뭔가 우울하고 복잡해"
})
check_response(res)

# 5. 활동 추가
res = requests.post(f"{base_url}/activities/", json={
    "user_id": user_id,
    "activity_type_id": activity_type_id,
    "description": "아침 조깅"
})
check_response(res)

# 6. 플로우 커브 추가
res = requests.post(f"{base_url}/flow-curve/", json={
    "user_id": user_id,
    "time_spent": 1.5,
    "satisfaction": 4.5
})
check_response(res)

# 7. 사용자 목록 조회
res = requests.get(f"{base_url}/users/")
check_response(res)
