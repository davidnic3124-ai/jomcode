import pytest

@pytest.mark.parametrize("value", [1,500])
def test_valid_capacity(value):
    assert type(value) is int and 1 <= value <= 500

