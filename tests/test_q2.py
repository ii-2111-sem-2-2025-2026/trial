import pytest
from src.quiz1 import q2_union_probability

def test_q2_union_probability():
    # Dari soal: P(A)=0.6, P(B)=0.5, P(A∩B)=0.3 -> P(A∪B)=0.8
    assert q2_union_probability(0.6, 0.5, 0.3) == pytest.approx(0.8)
