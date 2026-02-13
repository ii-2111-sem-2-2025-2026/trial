from src.quiz1 import q1_sample_space_binary_3

def test_q1_sample_space_binary_3():
    ss = q1_sample_space_binary_3()
    assert isinstance(ss, list)
    assert len(ss) == 8
    assert all(isinstance(x, tuple) and len(x) == 3 for x in ss)
    assert set(ss) == {
        (0,0,0),(0,0,1),(0,1,0),(0,1,1),
        (1,0,0),(1,0,1),(1,1,0),(1,1,1)
    }
