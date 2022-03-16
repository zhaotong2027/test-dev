import pytest


@pytest.fixture(scope="function", params=['张三', '李四'], name='aaa')
# @pytest.fixture(scope="class", autouse=True)
# @pytest.fixture(scope="module  ", autouse=True)
def my_fixture(request):
    print('前置方法，可实现全部或部分用例的后置')
    yield request.param  # return和yield都执行返回，yield后面可跟代码，return则不可
    print("后置方法，可实现全部或部分用例的后置")
    # return request.param  # 固定写法，fixture参数名带复数，request 属性名不带复数

class TestLogin:

    # def setup_class(self):
    #     print('\n每个类执行前的初始化，比如：创建日志，创建数据库，创建接口的请求对象\n')
    #
    # def setup(self):
    #     print('\n在执行测试用例之前的初始化')

    def test_01_login(self):
         print('测试登录')

    # def test_05_register(self, my_fixture):
    def test_05_register(self, aaa):
        print('测试注册')
        print('\n用户'+str(aaa)+'注册成功')

    # def teardown(self):
    #     print('\n在执行测试用例之后扫尾工作\n')
    #
    # def teardown_class(self):
    #     print('\n每个类执行结束的扫尾工作，比如：销毁对象\n')
