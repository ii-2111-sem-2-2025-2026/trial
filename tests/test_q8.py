import pytest
from src.quiz1 import q8_conditional_probability

def test_q8_conditional_probability():
    # Dari soal: 80 dari 150
    assert q8_conditional_probability(80, 150) == pytest.approx(80/150)
