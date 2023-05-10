import unittest
from config import BASE_DIR
from scripts.test_ihrm_login02 import Test02
from htmltestreport  import HTMLTestReport

# 创建测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test02))

runner=HTMLTestReport(BASE_DIR+"/reports/ihrm.html",title="IHRM人力资源管理系统接口测试报告")
runner.run(suite)