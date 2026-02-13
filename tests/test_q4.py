from src.quiz1 import q4_is_mutually_exclusive_possible

def test_q4_is_mutually_exclusive_possible():
    # Dari soal: 0.4+0.35+0.3=1.05 -> tidak mungkin mutually exclusive
    is_possible, total = q4_is_mutually_exclusive_possible([0.4, 0.35, 0.3])
    assert total == 1.05
    assert is_possible is False
