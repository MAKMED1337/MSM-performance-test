from typing import override

from py_ecc.typing import Point2D

from .interface import MSM, Point


class Naive(MSM):
    _points: list[Point2D]

    @override
    def compile(self, points: list[Point]) -> None:
        self._points = points

    def _pow(self, p: Point, b: int) -> Point:
        result = None
        while b:
            if b & 1:
                result = self._add(result, p)

            b >>= 1
            if b:
                p = self._square(p)
        return result

    @override
    def calculate(self, scalars: list[int]) -> Point:
        result = None
        for i, pw in enumerate(scalars):
            result = self._add(result, self._pow(self._points[i], pw))
        return result

    def __str__(self) -> str:
        return 'Naive'
