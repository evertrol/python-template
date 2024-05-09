"""Provide a set of integration functions"""

from collections.abc import Iterable
from math import isinf, isnan
from typing import Any, Callable


__all__ = ["integrate_simple"]


def integrate_simple(
    func: Callable[[float, ...], float],
    x1: float,
    x2: float,
    args: Iterable[Any] | None = None,
    dx: float = 1e-3,
):
    """A very simple and inaccurate integrating function

    Parameters
    ==========

    func: user-provided function to integrate. This function should
        take a value x as its first output, and return a value
        y. Other arguments can be provided as a tuple through the
        `args` keyword argument.

    x1, x2: start and end values of the integration interval.

    args: extra arguments provided to `func`, as an iterable.

    dx: relative step size in the interval x1 -- x2.

    """

    if isinf(x1) or isinf(x2) or isnan(x1) or isnan(x2):
        raise ValueError(
            "one of the integration interval boundaries is infite or not a number"
        )
    if x1 > x2:
        raise ValueError("x1 should be smaller than x2")
    if x1 < x2:
        dx = (x2 - x1) * dx
        x1 = x1 + dx / 2
    else:
        return 0

    if args is None:
        args = ()

    total: float = 0
    x: float = x1
    while x < x2:
        y = func(x, *args) * dx
        total += y
        x += dx

    return total
