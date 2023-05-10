import unittest
from api.ihrm_login_api import IhrmLoginApi
from common.assert_util import assert_util
from parameterized import parameterized
from common.read_json import read_json
from config import BASE_DIR


class Test(unittest.TestCase):
    # 参数化实现数据与脚本分离
    path_filename=BASE_DIR + "/data/ihrm_login.json"
    @parameterized.expand(read_json(path_filename))
    def test_login(self,rep_body,success,code,message):
        resp = IhrmLoginApi.login(rep_body)
        assert_util(self, resp, success, code, message)
        print(resp.json())


