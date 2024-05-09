from math import sqrt, inf, isnan, nan

from pytest import approx, raises

from myproject import differentiate_simple


def f1(x, c=0):
    return c * x**2 + x + 1


def f2(x):
    return sqrt(x)


def f3(x):
    return 1 / x


def test_differentiate_simple():
    y = differentiate_simple(f1, 0)
    assert y == approx(1)

    y = differentiate_simple(f1, inf)
    assert isnan(y)

    with raises(ValueError, match="x is not a number"):
        differentiate_simple(f1, nan)
    # Integrate beyond the domain of the function
    with raises(ValueError, match="math domain error"):
        differentiate_simple(f2, -1)
    with raises(ZeroDivisionError, match="division by zero"):
        differentiate_simple(f3, 0)
