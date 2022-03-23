import time


class TestProduct:
    # @pytest.mark.skip(reason="跳过休眠")
    def test_02_product(self, interface_fixture):
        time.sleep(3)
        print('测试产品')
        print('\n用户'+str(interface_fixture)+'看过产品')

