# test_solution.py
import pytest
from solution import add, multiply   # change to your module name

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(0, 100) == 0
    
    