from combiner import Combiner
from implementations import MSM, Naive, Pippenger, Point
from implementations.my import My
from random_helper import random_number, random_point

TRIES = 10
N = 24


def compile_and_run(msm: MSM, points: list[Point], scalars: list[int]) -> tuple[Point, Combiner, Combiner]:
    compiler = Combiner()
    msm.set_combiner(compiler)
    msm.compile(points)

    runner = Combiner()
    msm.set_combiner(runner)
    result = msm.calculate(scalars)

    return result, compiler, runner


def run_all_random(n: int, algos: list[MSM]) -> list[tuple[int, int]]:
    points = [random_point() for _ in range(n)]
    scalars = [random_number() for _ in range(n)]

    results = [compile_and_run(msm, points, scalars) for msm in algos]
    assert all(i[0] == results[0][0] for i in results)  # noqa: S101

    return [(i[1].get_stat(), i[2].get_stat()) for i in results]


def main() -> None:
    algos = [Naive(), Pippenger(4), Pippenger(5), Pippenger(6), My(4), My(6), My(8), My(12)]
    total = [[0, 0] for i in range(len(algos))]
    for _ in range(TRIES):
        stats = run_all_random(N, algos)
        for i in range(len(algos)):
            total[i][0] += stats[i][0]
            total[i][1] += stats[i][1]

    for algo, stat in zip(algos, total, strict=True):
        print(algo, stat)  # noqa: T201


if __name__ == '__main__':
    main()
