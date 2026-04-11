from math import ceil, floor, prod


def main(H):
    H = set(H)
    Theta = set(floor(eng / 3) for eng in H if eng >= 23 or eng <= -48)
    Phi = H | Theta

    Psi = {5 * phi for phi in Phi if phi > 49 or phi < 7}

    Xi = {(theta % 2) - floor(theta / 5)
          for theta in Theta if any(phi >= theta for phi in Phi)}

    B = {4 * xi - ceil(xi / 2) for xi in Xi if any(psi <= xi for psi in Psi)}

    sum_psi = sum(ceil(psi/3) for psi in Psi)
    prod_B = prod(beta for beta in B)

    kappa = sum_psi - prod_B
    return kappa


print(
    main({4, -59, -89, -21, 80, 18, 82, 26, -34, -97}),
    main({32, -63, 35, -93, -61, 8, -22, 44, 49, -41}),
    sep="\n"
)
