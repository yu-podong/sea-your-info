import requests
import json
from tkinter import messagebox

class Post_ch():
    def __init__(self, ID, Token, title, date, URL, tpye):
        self.ID = ID
        self.token = Token
        self.title =title
        self.date =date
        self.URL =URL
        self.type = tpye

    def delete_list_dept(self, string):
        # DB의 게시물을 삭제하는 코드 샘플입니다. 삭제할 게시물의 id가 필요합니다.
        # 실행전 확인 : URL 설정, ID 값 설정

        # Header : 데이터에 관한 설명
        headers = {
            'Authorization': 'Token '+self.token
        }

        # URL
        URL = "http://ras.studio1122.net:8000/posts/"
        # URL = "http://localhost:8000/posts/" # 자기 컴퓨터에서 서버를 실행한 경우

        # ID
        ID = self.ID  # 변수!!! 실행전 설정 필수!!!

        integratedURL = URL + ID + "/"

        # Request DELETE : id가 ID인 게시물을 삭제합니다.
        try:
            response = requests.delete(integratedURL, headers=headers)
        except:
            messagebox.showwarning("연결되어 있지 않음", "네트워크에 연결되지 않았거나, 불안정합니다.")
            return

        # 응답 코드, 텍스트 출력
        print("response")
        print(response.text)

        if not (response.text):
            string.append('OK')
        else :
            string.append('Fail')


    def delete_list_sw(self, string):
        # DB의 게시물을 삭제하는 코드 샘플입니다. 삭제할 게시물의 id가 필요합니다.
        # 실행전 확인 : URL 설정, ID 값 설정

        # Header : 데이터에 관한 설명
        headers = {
            'Authorization': 'Token '+self.token
        }

        # URL
        URL = "http://ras.studio1122.net:8000/posts_sw/"
        # URL = "http://localhost:8000/posts/" # 자기 컴퓨터에서 서버를 실행한 경우

        # ID
        ID = self.ID  # 변수!!! 실행전 설정 필수!!!

        integratedURL = URL + ID + "/"

        # Request DELETE : id가 ID인 게시물을 삭제합니다.
        try:
            response = requests.delete(integratedURL, headers=headers)
        except:
            messagebox.showwarning("연결되어 있지 않음", "네트워크에 연결되지 않았거나, 불안정합니다.")
            return

        # 응답 코드, 텍스트 출력
        print("response")
        print(response.text)

        if not (response.text):
            string.append('OK')
        else :
            string.append('Fail')


    def update_list_sw(self, string):
        # DB에 게시물을 수정하는 코드 샘플입니다.
        # 실행전 확인 : URL 설정, ID 값 설정

        # Header : 데이터에 관한 설명
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Token '+self.token
        }

        # URL : 목적지 URL
        URL = "http://ras.studio1122.net:8000/posts_sw/"
        # URL = "http://localhost:8000/posts/" # 자기 컴퓨터에서 서버를 실행한 경우

        # ID : 수정할 게시물의 id
        ID = self.ID  # 변수!!! 실행전 설정 필수!!!

        integratedURL = URL + ID + "/"

        # Data (Dictionary 타입) : 수정할 데이터
        data = {
            "title": self.title,
            "date": self.date,
            # Date(날짜) 필드는 UTC 시간으로 바꾸고(-9 hour), "YYYY-MM-DDTHH:MM:SS.000Z" 형식으로 전송 필요합니다.
            "url": self.URL,
            "type": self.type,
            "isSent": "True"
        }

        # Request PUT
        try:
            response = requests.put(integratedURL, data=json.dumps(data), headers=headers)
        except:
            messagebox.showwarning("연결되어 있지 않음", "네트워크에 연결되지 않았거나, 불안정합니다.")
            return

        # 응답 코드, 텍스트 출력
        print("status code : ", response.status_code)  # 성공 : 201
        print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열

        string.append(response.status_code)


    def update_list_dept(self, string):
        # DB에 게시물을 수정하는 코드 샘플입니다.
        # 실행전 확인 : URL 설정, ID 값 설정

        # Header : 데이터에 관한 설명
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Token '+self.token
        }

        # URL : 목적지 URL
        URL = "http://ras.studio1122.net:8000/posts/"
        # URL = "http://localhost:8000/posts/" # 자기 컴퓨터에서 서버를 실행한 경우

        # ID : 수정할 게시물의 id
        ID = self.ID  # 변수!!! 실행전 설정 필수!!!

        integratedURL = URL + ID + "/"

        # Data (Dictionary 타입) : 수정할 데이터
        data = {
            "title": self.title,
            "date": self.date,
            # Date(날짜) 필드는 UTC 시간으로 바꾸고(-9 hour), "YYYY-MM-DDTHH:MM:SS.000Z" 형식으로 전송 필요합니다.
            "url": self.URL,
            "type": self.type,
            "isSent": "True"
        }

        # Request PUT
        try:
            response = requests.put(integratedURL, data=json.dumps(data), headers=headers)
        except:
            messagebox.showwarning("연결되어 있지 않음", "네트워크에 연결되지 않았거나, 불안정합니다.")
            return

        # 응답 코드, 텍스트 출력
        print("status code : ", response.status_code)  # 성공 : 201
        print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열

        string.append(response.status_code)

