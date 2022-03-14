import time
import pytest

class TestProduct:
    @pytest.mark.skip(reason="跳过休眠")
    def test_02_product(self):
        time.sleep(3)
        print('测试产品')
