from math import ceil


def b_set(H):
    B = set()
    for eta in H:
        if not (-56 < eta <= 1):
            B.add(eta + eta**4)
    return B


def theta_set(H):
    Theta = set()
    for eta in H:
        if (-5 < eta < 45):
            Theta.add(eta % 3)
    return Theta


def m_set(Theta, B):
    return Theta | B


def n_set(M):
    N = set()
    for mu in M:
        if -95 <= mu <= 43:
            N.add(ceil(mu / 2))
    return N


def xi_set(B, M):
    Xi = set()
    for beta in B:
        for mu in M:
            if mu <= beta:
                Xi.add(beta * mu)
    return Xi


def main(H):
    B = b_set(H)
    Theta = theta_set(H)
    M = m_set(Theta, B)
    N = n_set(M)
    Xi = xi_set(B, M)

    product = 1
    for nu in N:
        product *= 4 * nu

    return len(Xi | N) + product

if __name__ == "__main__":
    print(main({-89, -25, 7, -51, -48, -12, -42, -72, -70, 62}))
    print(main({4, -27, 7, -56, 40, 75, -76, 86, 27, -99}))
