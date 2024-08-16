def cdiv(a: int, b: int) -> int:
    assert a >= 0 and b > 0  # noqa: S101, PT018
    return (a + b - 1) // b


def bits_to_num(bits: list[int]) -> int:
    result = 0
    for bit in reversed(bits):
        result = 2 * result + bit
    return result
