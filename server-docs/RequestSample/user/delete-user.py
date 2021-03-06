import requests
import json

# user를 삭제하는 코드 샘플입니다.
# 실행전 확인 : URL 설정, username 설정, token 설정, data

# Header : 데이터에 관한 설명
headers = {
    'Content-Type': 'application/json; charset=utf-8',
    'Authorization': 'Token XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'  # 해당 유저 토큰 or 관리자 토큰
}

# URL : 목적지 URL
URL = "http://ras.studio1122.net:8000/user/"
# URL = "http://localhost:8000/user/" # 자기 컴퓨터에서 서버를 실행한 경우

# Username
username = "normaluser"

integratedURL = URL + username + "/"

# Data (Dictionary 타입) : 전송할 데이터
data = {
    "username": "test",
    "password": "password"
}

# Request DELETE
response = requests.delete(URL, data=json.dumps(data), headers=headers)

# 응답 코드, 텍스트 출력
print("status code : ", response.status_code)   # 성공 : 201
print("response text : ", response.text)        # 응답 텍스트 : JSON 형식 문자열
