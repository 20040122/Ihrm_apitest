import unittest
from api.ihrm_emp_api import IhrmEmpApi
from common.assert_util import assert_util
from parameterized import parameterized
from common.get_header import get_header
from common.read_ejson import read_ejson
from config import BASE_DIR


class ITest(unittest.TestCase):
    path_filename=BASE_DIR+ "/data/ihrm_emp.json"
    @parameterized.expand(read_ejson(path_filename))
    def testcreate(self,json_Data,success,code,message):
         header=get_header()
         resp=IhrmEmpApi().add_emp(header,json_Data)
         assert_util(self,resp,success,code,message)

