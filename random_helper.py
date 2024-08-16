import secrets

from py_ecc.bn128.bn128_curve import G1, multiply

from implementations import Point

PRIME = 21888242871839275222246405745257275088696311157297823662689037894645226208583


def random_number() -> int:
    return secrets.randbelow(PRIME)


def random_point() -> Point:
    return multiply(G1, random_number())
