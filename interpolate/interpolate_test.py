from assertpy import assert_that
from interpolate.interpolate import interpolate
from interpolate.polynomial import Polynomial, ZERO
import pytest

EPSILON = 1e-9

@pytest.mark.parametrize('points', [
    [(1, 1), (2, 0), (-3, 2), (4, 4)],
    [(2, 7)],
    [(-2, 5), (3, -10)],
    [(-1, 0), (2, 0), (4, 0)],
])
def test_interpolate_passes_through_points(points):
    actual_polynomial = interpolate(points)
    expected_evaluations = points
    actual_evaluations = [(x, actual_polynomial(x))
                          for (x, y) in expected_evaluations]

    for (p1, p2) in zip(expected_evaluations, actual_evaluations):
        for (a, b) in zip(p1, p2):
            assert_that(a).is_close_to(b, EPSILON)


def test_polynomial_multiplication():
    product = Polynomial([2, -3]) * Polynomial([5, 4, 1])
    assert product.coefficients == [10, -7, -10, -3]
    assert (ZERO * Polynomial([5, 4, 1])).coefficients == []
    assert (Polynomial([2, -3]) * ZERO).coefficients == []
