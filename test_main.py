def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(a, b):
    return a / b

def multi(x, y):
    return x * y


def test_add():
    assert add(1, 3) == 4


def test_sub():
    assert sub(5, 3) == 2

def test_div():
    assert div(4, 2) == 2

def test_multi():
    assert multi(2, 3) == 6