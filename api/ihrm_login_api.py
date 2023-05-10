import requests
class IhrmLoginApi(object):
    @classmethod
    def login(cls,jsonData):
        resp=requests.post("http://ihrm-java.itheima.net/api/sys/login",
                            json=jsonData)
        return resp
