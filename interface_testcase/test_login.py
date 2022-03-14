import pytest

def test_04_func():
    print("测试函数")

class TestLogin:
    usernum = 1
    @pytest.mark.run(order=4)
    @pytest.mark.smoke
    def test_01_login(self):
        print('测试登录')

    @pytest.mark.run(order=1)
    @pytest.mark.usermanage
    def test_05_register(self):
        print('测试注册')
        # assert 1==2

    @pytest.mark.run(order=2)
    @pytest.mark.skip(usernum > 1, reason = "不可超过两人同时在线")
    def test_06_rename(self):
        print('测试重命名')

    @pytest.mark.run(order=3)
    @pytest.mark.smoke
    def test_07_change(self):
        print('测试修改')