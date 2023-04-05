from main import *
from lambda_func import *

def test_add():
    res = add(5, 5)
    assert res == 10

def test_substract():
    res = subtract(10, 5)
    assert res == 5

def test_multiply():
    res = multiply(5, 5)
    assert res == 25

def test_divide():
    res = divide(25, 3)
    assert res == 8

def test_get_ip():
    res = get_public_ip()
    assert len(res) > 0