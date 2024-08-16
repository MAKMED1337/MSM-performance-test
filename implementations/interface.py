from py_ecc.fields import bn128_FQ
from py_ecc.typing import Point2D

from combiner import Combiner

type Point = Point2D[bn128_FQ]

max_pw = 254


class MSM:
    _current_combiner: Combiner

    def __init__(self) -> None:
        self._current_combiner = Combiner()

    def compile(self, points: list[Point]) -> None:
        raise NotImplementedError

    def calculate(self, scalars: list[int]) -> Point:
        raise NotImplementedError

    def set_combiner(self, combiner: Combiner) -> None:
        self._current_combiner = combiner

    def get_combiner(self) -> Combiner:
        return self._current_combiner

    def _add(self, p1: Point, p2: Point) -> Point:
        return self._current_combiner.add(p1, p2)

    def _square(self, p: Point) -> Point:
        return self._current_combiner.square(p)
