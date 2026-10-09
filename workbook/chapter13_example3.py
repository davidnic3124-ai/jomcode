def remaining(capacity,registered):
    return capacity - registered

def test_remaining():
    assert remaining(100, 75) == 25
    assert remaining(50, 20) == 30
    assert remaining(200, 150) == 50
    assert remaining(0, 0) == 0
    assert remaining(10, 5) == 5   
