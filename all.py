import os
import pytest

# noinspection PyPackageRequirements
if __name__ == '__main__':
    # pytest.main(['-vs', '../interface_testcase', '--alluredir', 'result'])
    # os.system('allure generate ./result -o ./report --clean')
    pytest.main(['-vs', './interface_testcase', '--alluredir', 'temp'])
    os.system('allure generate ./temp -o ./report --clean')
    # pytest.main(['-vs', '../interface_testcase', '--reruns=2'])
    # pytest.main(['-vs', '../interface_testcase', '-n 2'])
    # pytest.main(['-vs', '../interface_testcase/test_login.py::TestLogin::test_01_login'])
    # pytest.main(['-vs', '../interface_testcase/test_login.py::test_04_func'])
    # pytest.ma in(['-vs', '../web_test  case'])