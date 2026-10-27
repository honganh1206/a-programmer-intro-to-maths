import pytest

from gradient.gradient_descent import f, gradient, gradient_descent, gss, steepest_descent


def test_f():
    assert f([2, 3]) == 22


def test_gradient():
    assert gradient(f, [2.0, 3.0]) == pytest.approx([4, 12])


@pytest.mark.parametrize('center, a, b', [(2, 1, 5), (-3, -6, 0)])
def test_gss(center, a, b):
    minimum = gss(lambda x: (x - center)**2, a, b, tol=1e-6)

    assert minimum == pytest.approx(center, abs=1e-6)


def test_gradient_descent():
    point, value, history = gradient_descent(f, [2.0, 1.0])

    assert point == pytest.approx([0, 0], abs=1e-6)
    assert value == pytest.approx(0, abs=1e-6)
    assert history[0] == [2.0, 1.0]
    assert history[-1] == pytest.approx(point)


def test_steepest_descent():
    point, value, history = steepest_descent(
        f, lambda x: [2*x[0], 4*x[1]], [2.0, 1.0],
    )

    assert point == pytest.approx([0, 0], abs=1e-6)
    assert value == pytest.approx(0, abs=1e-6)
    assert history[0] == pytest.approx([2.0, 1.0])
    assert history[-1] == pytest.approx(point)
