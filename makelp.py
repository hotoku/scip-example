# LPファイルを作る

import itertools as it


def build_objective(demands: list[int], vars: list[str], adjust: float = 1.0) -> str:
    assert len(demands) == len(vars)
    n = len(demands)
    coef_linear = str(adjust / n)
    # LPファイルの制約で、2次の項の計数は2倍にしておく
    coef_square = str(2/n - 2/n**2)
    coef_cross = str(- 4 / n**2)
    linears = " + ".join([f"{coef_linear} {vars[i]}"
                          for i in range(n)])
    squares = " + ".join([f"{coef_square} {vars[i]}^2"
                          for i in range(n)])
    crosses = " ".join([f"{coef_cross} {vars[i]}*{vars[j]}"
                        for i, j in it.product(range(n), range(n))
                        if i < j])
    return f"{linears} + [ {squares} {crosses} ] /2"


def mysum(xs: list[int]) -> int:
    ret = 0
    for x in xs:
        ret += x
    return ret


def build_constraints(demands: list[int], vars: list[str]) -> list[str]:
    assert len(demands) == len(vars)
    n = len(demands)
    return [
        f"{' + '.join(vars[:i])} > {mysum(demands[:i])}"
        for i in range(1, n + 1)
    ]


def join_plus(x: list[str], i: int) -> str:
    return " + ".join(x[:i])


def partial_sum(d: list[int], i: int) -> int:
    ret = 0
    for j in range(i):
        ret += d[j]
    return ret


def main() -> None:
    d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(d)
    x = [f"x{i}" for i in range(n)]
    a = 1

    # 目的関数の記述
    obj_linear = ""
    for i in range(n):
        obj_linear += f" + {a/n} {x[i]}"

    obj_square = ""
    for i in range(n):
        obj_square += f" + {2/n - 2/n**2} {x[i]}^2"

    obj_cross = ""
    for i, j in it.product(range(n), range(n)):
        if i < j:
            obj_cross += f" - {4/n**2} {x[i]} * {x[j]}"

    obj_line = f"minimize {obj_linear} + [ {obj_square} {obj_cross} ] / 2"

    # 制約条件の記述
    cons = []
    cons.append("subject to")
    for i in range(n):
        cons.append(
            f"constraint{i}: {join_plus(x, i+1)} > {partial_sum(d, i)}")

    print(obj_line)
    print()
    print("\n".join(cons))


if __name__ == "__main__":
    main()
