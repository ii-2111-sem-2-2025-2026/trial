import pytest
from src.quiz1 import q7_demorgan_notA_and_notB

def test_q7_demorgan_notA_and_notB():
    # Dari soal: P(A∪B)=0.8 -> P(Ac ∩ Bc)=0.2
    assert q7_demorgan_notA_and_notB(0.8) == pytest.approx(0.2)
