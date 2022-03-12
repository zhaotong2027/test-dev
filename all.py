import pytest

if __name__ == '__main__':
    pytest.main(['-vs', '../interface_testcase', '--reruns=2'])
    # pytest.main(['-vs', '../interface_testcase', '-n 2'])
    # pytest.main(['-vs', '../interface_testcase/test_login.py::TestLogin::test_01_login'])
    # pytest.main(['-vs', '../interface_testcase/test_login.py::test_04_func'])
    # pytest.main(['-vs', '../web_test  case'])