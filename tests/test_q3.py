import pytest
from src.quiz1 import q3_complement_probability

def test_q3_complement_probability():
    # Dari soal: P(lolos)=0.85 -> P(gagal)=0.15
    assert q3_complement_probability(0.85) == pytest.approx(0.15)
