from assertpy import assert_that
from interpolate.bezier import bezier, bezier_derivative
import pytest

EPSILON = 1e-9


@pytest.mark.parametrize('points', [
    [(2, 7)],
    [(-2, 5), (3, -10)],
    [(0, 1), (2, 5), (6, -3)],
    [(0, 0), (1, 3), (3, 3), (4, 0)],
])
def test_bezier_passes_through_endpoints(points):
    expected_evaluations = [points[0], points[-1]]
    actual_evaluations = [bezier(0, points), bezier(1, points)]

    for (p1, p2) in zip(expected_evaluations, actual_evaluations):
        for (a, b) in zip(p1, p2):
            assert_that(a).is_close_to(b, EPSILON)


@pytest.mark.parametrize('t', [0, 0.25, 0.5, 0.75, 1])
def test_bezier_with_one_point_is_constant(t):
    expected_evaluation = (2, -7)
    actual_evaluation = bezier(t, [expected_evaluation])

    for (a, b) in zip(expected_evaluation, actual_evaluation):
        assert_that(a).is_close_to(b, EPSILON)


@pytest.mark.parametrize('points, t, expected_evaluation', [
    ([(-2, 5), (6, -3)], 0.25, (0, 3)),
    ([(0, 1), (2, 5), (6, -3)], 0.25, (1.125, 2.25)),
    ([(0, 0), (1, 3), (3, 3), (4, 0)], 0.25, (0.90625, 1.6875)),
    ([(0, 0), (1, 3), (3, 3), (4, 0)], 0.5, (2, 2.25)),
])
def test_bezier_evaluates_curve(points, t, expected_evaluation):
    actual_evaluation = bezier(t, points)

    for (a, b) in zip(expected_evaluation, actual_evaluation):
        assert_that(a).is_close_to(b, EPSILON)


@pytest.mark.parametrize('t', [0, 0.25, 0.5, 0.75, 1])
def test_bezier_derivative_with_one_point_is_zero(t):
    expected_evaluation = (0, 0)
    actual_evaluation = bezier_derivative(t, [(2, -7)])

    for (a, b) in zip(expected_evaluation, actual_evaluation):
        assert_that(a).is_close_to(b, EPSILON)


@pytest.mark.parametrize('points, t, expected_evaluation', [
    ([(-2, 5), (6, -3)], 0, (8, -8)),
    ([(-2, 5), (6, -3)], 0.25, (8, -8)),
    ([(-2, 5), (6, -3)], 1, (8, -8)),
    ([(0, 1), (2, 5), (6, -3)], 0, (4, 8)),
    ([(0, 1), (2, 5), (6, -3)], 0.25, (5, 2)),
    ([(0, 1), (2, 5), (6, -3)], 1, (8, -16)),
    ([(0, 0), (1, 3), (3, 3), (4, 0)], 0, (3, 9)),
    ([(0, 0), (1, 3), (3, 3), (4, 0)], 0.25, (4.125, 4.5)),
    ([(0, 0), (1, 3), (3, 3), (4, 0)], 1, (3, -9)),
])
def test_bezier_derivative_evaluates_tangent(points, t, expected_evaluation):
    actual_evaluation = bezier_derivative(t, points)

    for (a, b) in zip(expected_evaluation, actual_evaluation):
        assert_that(a).is_close_to(b, EPSILON)
