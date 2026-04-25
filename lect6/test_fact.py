import pytest

def fact(n):
    if n in range(0, 1):
        return 1
    return n * fact(n-1)

def test_fact():
    assert fact(5) == 120
    assert fact(0) == 1
    with pytest.raises(RecursionError):
        fact(-1)
