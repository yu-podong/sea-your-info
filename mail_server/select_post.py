def School(lst_Dep=[]):
    import requests
    import json
    # DB의 게시물들을 읽어오는 코드 샘플입니다.
    # 실행전 확인 : URL 설정
    # URL : 목적지 URL

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Token 76042b6aa0deb34d25aa58eafb82a0425f07f433'  # 서버가 변경되면 토큰이 변경되므로 authorization 수정 필요합니다.
    }

    URL = "http://ras.studio1122.net:8000/posts/"

    # Request GET
    response_Dep = requests.get(URL)

    # 응답 코드, 텍스트 출력
    print("status code : ", response_Dep.status_code)  # 성공 : 200
    print("response text : ", response_Dep.text)  # 응답 텍스트 : JSON 형식 문자열

    # JSON 형식 문자열을 Dictionary 타입(Dictionary 타입 배열)으로 변환
    response_dict = json.loads(response_Dep.text)

    for i in range(0, len(response_dict)):
        if response_dict[i]['isSent'] == False:
            lst_Dep.append(response_dict[i])

    for i in range(len(lst_Dep)):
        data = {  # 데이터 전송 후 isSent True로 바꿔주기 위한 코드
            "title": lst_Dep[i]['title'],
            "date": lst_Dep[i]['date'],
            "url": lst_Dep[i]['url'],
            "type": lst_Dep[i]['type'],
            "isSent": "True"
        }
        integratedURL = URL + str(lst_Dep[i]['id']) + "/"  # 서버로 데이트 전송하는 코드
        response = requests.put(integratedURL, data=json.dumps(data), headers=headers)  # 서버로 데이트 전송하는 코드

    return lst_Dep


# sw학과 공지사항
def Software(lst_sw=[]):
    import requests
    import json
    # DB의 게시물들을 읽어오는 코드 샘플입니다.
    # 실행전 확인 : URL 설정
    # URL : 목적지 URL

    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'Authorization': 'Token 76042b6aa0deb34d25aa58eafb82a0425f07f433'  # 서버가 변경되면 토큰이 변경되므로 authorization 수정 필요합니다.
    }

    URL = "http://ras.studio1122.net:8000/posts_sw/"

    # Request GET
    response_sw = requests.get(URL)

    # 응답 코드, 텍스트 출력
    print("status code : ", response_sw.status_code)  # 성공 : 200
    print("response text : ", response_sw.text)  # 응답 텍스트 : JSON 형식 문자열

    # JSON 형식 문자열을 Dictionary 타입(Dictionary 타입 배열)으로 변환
    response_dict_sw = json.loads(response_sw.text)

    for i in range(0, len(response_dict_sw)):
        if response_dict_sw[i]['isSent'] == False:
            lst_sw.append(response_dict_sw[i])

    for i in range(len(lst_sw)):
        data = {  # 데이터 전송 후 isSent True로 바꿔주기 위한 코드
            "title": lst_sw[i]['title'],
            "date": lst_sw[i]['date'],
            "url": lst_sw[i]['url'],
            "type": lst_sw[i]['type'],
            "isSent": "True"
        }
        integratedURL = URL + str(lst_sw[i]['id']) + "/"  # 서버로 데이트 전송하는 코드
        response = requests.put(integratedURL, data=json.dumps(data), headers=headers)  # 서버로 데이트 전송하는 코드

    return lst_sw