# Задача 7. Вычисление дерева решений
# Способ 1

def main(x):
    table = {
        ('PIKE', 'ADA', 'XSLT'): 0,
        ('PIKE', 'ADA', 'FANCY'): 4,
        ('PIKE', 'ADA', 'IDL', 1970): 1,
        ('PIKE', 'ADA', 'IDL', 1967): 2,
        ('PIKE', 'ADA', 'IDL', 1992): 3,
        ('PIKE', 'CUDA', 2010): 5,
        ('PIKE', 'CUDA', 1999): 6,
        ('NIT', 'ADA'): 7,
        ('NIT', 'CUDA', 2010): 8,
        ('NIT', 'CUDA', 1999): 9
    }

    key = (x[0], x[1], x[2])
    if key in table:
        return table[key]

    key = (x[0], x[1], x[2], x[4])
    if key in table:
        return table[key]

    key = (x[0], x[1], x[3])
    if key in table:
        return table[key]

    return table[(x[0], x[1])]

print(
    main(['PIKE', 'ADA', 'XSLT', 2010, 1967]),
    main(['NIT', 'CUDA', 'XSLT', 1999, 1992]),
    main(['NIT', 'ADA', 'FANCY', 1999, 1970]),
    main(['PIKE', 'ADA', 'FANCY', 2010, 1970]),
    main(['PIKE', 'CUDA', 'XSLT', 1999, 1967]),
    sep='\n'
)
