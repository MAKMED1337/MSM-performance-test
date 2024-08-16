from typing import override

from .helper import bits_to_num, cdiv
from .interface import MSM, Point, max_pw


class My(MSM):
    _blocks: list[list[Point]]
    c: int

    def __init__(self, c: int) -> None:
        super().__init__()
        self.c = c

    def _calculate_masks(self, points: list[Point]) -> list[Point]:
        n = len(points)
        result: list[Point] = [None] * (1 << n)

        for i in range(1, 1 << n):
            for j in range(n):
                if i >> j & 1:
                    result[i] = self._add(result[i ^ (1 << j)], points[j])
                    break
        return result

    @override
    def compile(self, points: list[Point]) -> None:
        n = len(points)
        blocks = cdiv(n, self.c)
        self._blocks = [[None]] * blocks
        for i in range(blocks):
            self._blocks[i] = self._calculate_masks(points[i * self.c : (i + 1) * self.c])

    @override
    def calculate(self, scalars: list[int]) -> Point:
        result = None
        for i in range(max_pw - 1, -1, -1):
            result = self._square(result)
            bits = [s >> i & 1 for s in scalars]

            for j, blk in enumerate(self._blocks):
                num = bits_to_num(bits[j * self.c : (j + 1) * self.c])
                result = self._add(result, blk[num])

        return result

    def __str__(self) -> str:
        return f'My({self.c})'
