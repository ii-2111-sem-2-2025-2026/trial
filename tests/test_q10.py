import pytest
from src.quiz1 import q10_empirical_probability_greater_than

def test_q10_empirical_probability_greater_than():
    data = [20, 28, 29, 30, 31, 25]  # contoh data (input test)
    # nilai > 28: 29,30,31 -> 3/6
    assert q10_empirical_probability_greater_than(data, 28) == pytest.approx(3/6)
