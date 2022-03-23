import pytest


@pytest.fixture(scope="function", params=['张三', '李四'])
# @pytest.fixture(scope="function", params=['张三', '李四'], name='aaa')
# @pytest.fixture(scope="class", autouse=True)
# @pytest.fixture(scope="module", autouse=True)
def interface_fixture(request):
    print('\n接口前置方法，可实现全部或部分用例的后置')
    yield request.param  # return和yield都执行返回，yield后面可跟代码，return则不可
    print('\n接口后置方法，可实现全部或部分用例的后置')
    # return request.param  # 固定写法，fixture参数名带复数，request 属性名不带复数
