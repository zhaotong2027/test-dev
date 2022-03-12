import pytest

if __name__ == '__main__':
    # pytest.main(['-vs'])
    pytest.main(['-vs', 'test_login.py'])
    # pytest.main(['-vs', 'test_login.py', '-n 2'])