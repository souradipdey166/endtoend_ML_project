from check import add, dev

def test_add():
    assert add(2, 3) == 5

def test_dev():
    assert dev(10, 3) == 3