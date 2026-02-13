from src.quiz1 import q9_total_sample_points_board_test

def test_q9_total_sample_points_board_test():
    # Dari soal: 1 (lolos) + 5 tipe cacat
    assert q9_total_sample_points_board_test(5) == 6
