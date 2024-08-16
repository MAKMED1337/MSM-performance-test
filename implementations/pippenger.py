from typing import override

from .helper import cdiv
from .interface import MSM, Point, max_pw


class Pippenger(MSM):
    _points: list[Point]
    c: int

    def __init__(self, c: int) -> None:
        super().__init__()
        self.c = c

    @override
    def compile(self, points: list[Point]) -> None:
        self._points = points

    def _calculate_window(self, scalars: list[int]) -> Point:
        buckets: list[Point] = [None] * (1 << self.c)
        for i, pw in enumerate(scalars):
            buckets[pw] = self._add(buckets[pw], self._points[i])

        suff = None
        result = None

        for i in range((1 << self.c) - 1, 0, -1):
            suff = self._add(suff, buckets[i])
            result = self._add(result, suff)
        return result

    @override
    def calculate(self, scalars: list[int]) -> Point:
        result = None
        for i in range(cdiv(max_pw, self.c), -1, -1):
            for _ in range(self.c):
                result = self._square(result)

            bits = [(s >> (i * self.c)) % (1 << self.c) for s in scalars]
            result = self._add(result, self._calculate_window(bits))
        return result

    def __str__(self) -> str:
        return f'Pappenger({self.c})'
