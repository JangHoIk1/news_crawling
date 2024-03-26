import requests
# requests는 Python용 HTTP 라이브러리이다.
# 특정 웹사이트에 HTTP 요청을 보내 HTML 문서를 받아올 수 있는 라이브러리이다
# 웹페이지의 HTML 문서를 받아와서 텍스트 파일로 저장하는 코드

r = requests.get("https://naver.com")
# url 주소로 Get 요청을 보냈고, 서버로부터의 응답을 객체로 반환
with open("naver.txt","w") as f:
    f.write(r.text)

# open() 함수를 사용하여 파일을 열고, 여기서 naver.txt라는 파일을 쓰기 모드 w로 염
# 파일을 열때 with 문을 사용하면, 파일 사용이 끝난 후 자동으로 파일을 닫아준다
# 파일 핸들을 'f'라는 변수에 할당

