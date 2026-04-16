# Задача 6.
# Способ 1

from math import ceil
from functools import reduce


def main(H):
    H = set(H)
    B = set(
        map(
            lambda eta: eta + eta**4,
            filter(lambda eta: eta > 1 or eta <= -56, H)
        )
    )
    Theta = set(
        map(
            lambda eta: eta % 3,
            filter(lambda eta: -5 < eta < 45, H)
        )
    )
    M = Theta | B
    N = set(
        map(
            lambda mu: ceil(mu / 2),
            filter(lambda mu: -95 <= mu <= 43, M)
        )
    )
    Xi = set(
        map(
            lambda pair: pair[0] * pair[1],
            filter(
                lambda pair: pair[0] >= pair[1],
                ((beta, mu) for beta in B for mu in M)
            )
        )
    )

    product = reduce(lambda a, b: a*(4*b), N, 1)

    return len(Xi | N) + product


if __name__ == "__main__":
    print(main({-89, -25, 7, -51, -48, -12, -42, -72, -70, 62}))
    print(main({4, -27, 7, -56, 40, 75, -76, 86, 27, -99}))
