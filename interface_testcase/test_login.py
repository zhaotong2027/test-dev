
class TestLogin:

    # def setup_class(self):
    #     print('\n每个类执行前的初始化，比如：创建日志，创建数据库，创建接口的请求对象\n')
    #
    # def setup(self):
    #     print('\n在执行测试用例之前的初始化')

    def test_01_login(self):
         print('测试登录')

    def test_05_register(self, globle_fixture, interface_fixture):
    # def test_05_register(self, aaa):
        print('测试注册')
        print('\n用户'+str(globle_fixture)+'注册成功')

    # def teardown(self):
    #     print('\n在执行测试用例之后扫尾工作\n')
    #
    # def teardown_class(self):
    #     print('\n每个类执行结束的扫尾工作，比如：销毁对象\n')
