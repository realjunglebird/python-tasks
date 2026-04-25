# Задача 7. Вычисление дерева решений
# Способ 1/4

def zero(x, left, right):
    if x[0] == 'PIKE':
        return right
    if x[0] == 'NIT':
        return left


def one(x, left, right):
    if x[1] == 'ADA':
        return right
    if x[1] == 'CUDA':
        return left


def two(x, a, b, c):
    if x[2] == 'XSLT':
        return a
    if x[2] == 'IDL':
        return b
    if x[2] == 'FANCY':
        return c


def three(x, a, b):
    if x[3] == 2010:
        return a
    if x[3] == 1999:
        return b


def four(x, a, b, c):
    if x[4] == 1970:
        return a
    if x[4] == 1967:
        return b
    if x[4] == 1992:
        return c


def main(x):
    return zero(
        x,
        one(
            x,
            three(x, 8, 9),
            7
        ),
        one(
            x,
            three(x, 5, 6),
            two(x, 0, four(x, 1, 2, 3), 4)
        )
    )

print(
    main(['PIKE', 'ADA', 'XSLT', 2010, 1967]),
    main(['NIT', 'CUDA', 'XSLT', 1999, 1992]),
    main(['NIT', 'ADA', 'FANCY', 1999, 1970]),
    main(['PIKE', 'ADA', 'FANCY', 2010, 1970]),
    main(['PIKE', 'CUDA', 'XSLT', 1999, 1967]),
    sep='\n'
)
