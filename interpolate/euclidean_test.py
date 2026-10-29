import pytest

from interpolate.euclidean import extended_gcd


@pytest.mark.parametrize('a, b, expected_gcd', [
    (0, 0, 0),
    (9, 0, 9),
    (0, 9, 9),
    (12, 12, 12),
    (30, 18, 6),
    (7, 3, 1),
])
def test_extended_gcd(a, b, expected_gcd):
    gcd, x, y = extended_gcd(a, b)

    assert gcd == expected_gcd
    assert a * x + b * y == gcd
