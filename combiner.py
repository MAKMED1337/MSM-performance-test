from py_ecc.bn128.bn128_curve import add, double
from py_ecc.typing import (
    Field,
    Point2D,
)


class Combiner:
    _additions = 0
    _squarings = 0

    def add(self, p1: Point2D[Field], p2: Point2D[Field]) -> Point2D[Field]:
        self._additions += p1 is not None and p2 is not None
        return add(p1, p2)

    def square(self, p: Point2D[Field]) -> Point2D[Field]:
        self._squarings += p is not None
        return double(p)

    def get_stat(self) -> int:
        return self._additions + self._squarings
