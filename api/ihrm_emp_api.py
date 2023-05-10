import requests
class IhrmEmpApi(object):
    def add_emp(self,header,jsonData):
        resp=requests.post("http://ihrm-java.itheima.net/api/sys/user",
                            headers=header,
                            json=jsonData)
        return resp