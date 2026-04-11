# Задача 7. Вычисление дерева решений
# Способ 3?

def zero(x, a, b):
    match x[0]:
        case 'NIT':
            return a
        case 'PIKE':
            return b


def one(x, a, b):
    match x[1]:
        case 'CUDA':
            return a
        case 'ADA':
            return b


def two(x, a, b, c):
    match x[2]:
        case 'XSLT':
            return a
        case 'IDL':
            return b
        case 'FANCY':
            return c


def three(x, a, b):
    match x[3]:
        case 2010:
            return a
        case 1999:
            return b


def four(x, a, b, c):
    match x[4]:
        case 1970:
            return a
        case 1967:
            return b
        case 1992:
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
