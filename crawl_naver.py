import requests


r = requests.get("https://naver.com")
with open("naver.txt","w") as f:
    f.write(r.text)

    