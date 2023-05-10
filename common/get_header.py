import requests


def get_header():
    url="http://ihrm-java.itheima.net/api/sys/login"
    data={"mobile":"13800000002","password":"123456"}
    resp=requests.post(url,json=data)
    token=resp.json().get("data")
    header = {"Content-Type": "application/json",
              "Authorization": token}
    return header
