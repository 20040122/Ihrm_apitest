import unittest
import jsonschema
from api.ihrm_login_api import IhrmLoginApi
from parameterized import parameterized
from common.read_json import read_json
from config import BASE_DIR


# 全量字段校验
class Test02(unittest.TestCase):
    # 参数化实现数据与脚本分离
    path_filename = BASE_DIR + "/data/ihrm_login.json"
    @parameterized.expand(read_json(path_filename))
    def test_login(self,rep_body,success,code,message):
        resp = IhrmLoginApi.login(rep_body)
        schema={
            "type":"object",
            "properties":{
                "success":{"type":"boolean"},
                "code":{"type":"integer"},
                "message":{"type":"string"}
            },
            "required":["success","code","message"]
        }
        jsonschema.validate(instance=resp.json(),schema=schema)


