from math import sqrt, inf, nan

from pytest import approx, raises

from myproject import integrate_simple


def f1(x, c=0):
    return c * x**2 + x + 1


def f2(x):
    return sqrt(x)


def test_integrate_simple():
    y = integrate_simple(f1, 0, 1)
    assert y == approx(y, 1.5)

    y = integrate_simple(f1, -1, 1)
    assert y == approx(2)

    y = integrate_simple(f1, 0, 1, args=(3,))
    assert y == approx(2.5)

    y = integrate_simple(f2, 0, 1)
    assert y == approx(2 / 3, abs=1e-5)

    y = integrate_simple(f2, 0, 1, dx=1)
    assert y == approx(sqrt(0.5))

    with raises(ValueError, match="x1 should be smaller than x2"):
        integrate_simple(f1, 1, 0)
    with raises(
        ValueError,
        match="one of the integration interval " "boundaries is infite or not a number",
    ):
        integrate_simple(f1, -inf, 0)
    with raises(
        ValueError,
        match="one of the integration interval " "boundaries is infite or not a number",
    ):
        integrate_simple(f1, 0, nan)
    # Integrate beyond the domain of the function
    with raises(ValueError, match="math domain error"):
        integrate_simple(f2, -1, 1)
