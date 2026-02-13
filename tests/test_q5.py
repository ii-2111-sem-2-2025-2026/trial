import pytest
from src.quiz1 import q5_joint_probability

def test_q5_joint_probability():
    # Dari soal: 70 dari 100
    assert q5_joint_probability(70, 100) == pytest.approx(0.70)
