# Задача 6.
# Способ 1

from math import ceil


def main(H):
    H = set(H)
    B = {eta + eta**4 for eta in H if eta > 1 or eta <= -56}
    Theta = {eta % 3 for eta in H if -5 < eta < 45}
    M = Theta | B
    N = {ceil(mu / 2) for mu in M if -95 <= mu <= 43}
    Xi = {beta * mu for beta in B for mu in M if beta >= mu}

    product = 1
    for nu in N:
        product *= 4 * nu

    return len(Xi | N) + product


if __name__ == "__main__":
    print(main({-89, -25, 7, -51, -48, -12, -42, -72, -70, 62}))
    print(main({4, -27, 7, -56, 40, 75, -76, 86, 27, -99}))
