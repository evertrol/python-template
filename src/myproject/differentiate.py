"""Provide a set of differentiation functions"""

from collections.abc import Iterable
from math import isnan
from typing import Any, Callable


__all__ = ["differentiate_simple"]


def differentiate_simple(
    func: Callable[[float, ...], float],
    x: float,
    args: Iterable[Any] | None = None,
    dx: float = 1e-6,
):
    """A very simple and inaccurate differentiation function

    Parameters
    ==========

    func: user-provided function to differentiate. This function should
        take a value x as its first output, and return a value
        y. Other arguments can be provided as a tuple through the
        `args` keyword argument.

    x: value at which to provide the derivative

    args: extra arguments provided to `func`, as an iterable.

    dx: relative step size at x

    """

    if isnan(x):
        raise ValueError("x is not a number")

    if args is None:
        args = ()

    return (func(x + dx, *args) - func(x, *args)) / dx
