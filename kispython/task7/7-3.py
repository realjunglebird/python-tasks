# Задача 7. Вычисление дерева решений
# Способ 1

def main(x):
    if (x[0], x[1]) == ('NIT', 'ADA'):
        return 7

    table = {
        ('PIKE', 'ADA', 'XSLT'): 0,
        ('PIKE', 'ADA', 'FANCY'): 4,
    }

    key = (x[0], x[1], x[2])
    if key in table:
        return table[key]

    if (x[0], x[1]) == ('PIKE', 'ADA'):
        return {1970: 1, 1967: 2, 1992: 3}[x[4]]

    if (x[0], x[1]) == ('PIKE', 'CUDA'):
        return {2010: 5, 1999: 6}[x[3]]

    if (x[0], x[1]) == ('NIT', 'CUDA'):
        return {2010: 8, 1999: 9}[x[3]]


print(
    main(['PIKE', 'ADA', 'XSLT', 2010, 1967]),
    main(['NIT', 'CUDA', 'XSLT', 1999, 1992]),
    main(['NIT', 'ADA', 'FANCY', 1999, 1970]),
    main(['PIKE', 'ADA', 'FANCY', 2010, 1970]),
    main(['PIKE', 'CUDA', 'XSLT', 1999, 1967]),
    sep='\n'
)
