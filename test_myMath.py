import myMath

def test_zero():
    assert myMath.add(0,0) == 0

def test_add():
    assert myMath.add(2,2) == 4
    assert myMath.add(3,3) == 6

def test_add_2():
    assert myMath.add(2,2) == 4