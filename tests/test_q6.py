import pytest
from src.quiz1 import q6_marginal_probability

def test_q6_marginal_probability():
    # Dari soal: guncang rendah = 9 + 5 dari 100
    assert q6_marginal_probability([9, 5], 100) == pytest.approx(0.14)
