from tkinter import messagebox

class Login():
    def __init__(self, id, pw):
        self.id = id
        self.pw = pw

    def Check_SuperUser(self):
        import requests
        import json
        global str_token
        # user의 token으로 슈퍼 유저인지 확인하는 샘플 코드입니다.

        # 실행전 확인 : URL 설정, token

        # Header : 데이터에 관한 설명
        headers = {
            'Content-Type': 'application/json; charset=utf-8',
            'Authorization': 'Token ' + str_token
        }

        # URL : 목적지 URL
        URL = "http://ras.studio1122.net:8000/issuperuser/"
        # URL = "http://localhost:8000/issuperuser/" # 자기 컴퓨터에서 서버를 실행한 경우

        # Request POST
        try:
            response = requests.post(URL, headers=headers)
        except:
            messagebox.showwarning("연결되어 있지 않음", "네트워크에 연결되지 않았거나, 불안정합니다.")
            return

        response_dict2 = json.loads(response.text)  # 성공 실패 여부를 보기 위해서 딕셔너리로 변경
        # 응답 코드, 텍스트 출력
        print("status code : ", response.status_code)  # 성공 : 200
        print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열

        if response_dict2["is_super"]:  # 슈퍼유저인지 판단하는 코드
            return 1
        else:
            return 2

    def Check(self, string=[]):
        import requests
        import json
        global str_token
        # user의 token을 읽어오는 샘플 코드입니다. (로그인)
        # username과 password를 전송해 token을 받아오면, 해당 토큰을 통해 user임을 확인 받습니다.

        # 실행전 확인 : URL 설정, data

        # Header : 데이터에 관한 설명
        headers = {
            'Content-Type': 'application/json; charset=utf-8'
        }

        # URL : 목적지 URL
        URL = "http://ras.studio1122.net:8000/auth/"
        # URL = "http://localhost:8000/auth/" # 자기 컴퓨터에서 서버를 실행한 경우

        # Data (Dictionary 타입) : 전송할 데이터
        data = {
            "username": self.id,
            "password": self.pw,
        }

        # Request POST
        try:
            response = requests.post(URL, data=json.dumps(data), headers=headers)
        except:
            messagebox.showwarning("연결되어 있지 않음", "네트워크에 연결되지 않았거나, 불안정합니다.")
            return

        # 응답 코드, 텍스트 출력
        print("status code : ", response.status_code)  # 성공 : 201
        print("response text : ", response.text)  # 응답 텍스트 : JSON 형식 문자열

        # JSON 형식 문자열을 Dictionary 타입(Dictionary 타입 배열)으로 변환
        response_dict = json.loads(response.text)

        num = response.status_code
        string.append(num)
        string.insert(0, 2)
        for key in response_dict.keys():
            if key != "token":
                response_dict[key] = str(response_dict[key]).replace("[\'", "")
                response_dict[key] = str(response_dict[key]).replace("\']", "")
                string.append(key + " : " + response_dict[key])

        # 토큰
        if 'token' in list(response_dict.keys()):  # response_dict에 'token' 키를 가진 쌍이 있는지 확인
            str_token = response_dict['token']
            string[0] = self.Check_SuperUser()
            string.append(str_token)
