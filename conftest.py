import pytest


@pytest.fixture(scope="function", params=['王五', '赵六'])
# @pytest.fixture(scope="function", params=['张三', '李四'], name='aaa')
# @pytest.fixture(scope="class", autouse=True)
# @pytest.fixture(scope="module", autouse=True)
def globle_fixture(request):
    print('\n全局前置')
    yield request.param  # return和yield都执行返回，yield后面可跟代码，return则不可
    print('\n全局后置')
    # return request.param  # 固定写法，fixture参数名带复数，request 属性名不带复数
