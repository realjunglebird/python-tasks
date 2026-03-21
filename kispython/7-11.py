# Задача 7. Вычисление дерева решений
# Способ 2

def main(x):
    table = (
        {'PIKE', 'ADA', 'XSLT'},
        {'PIKE', 'ADA', 'IDL', 1970},
        {'PIKE', 'ADA', 'IDL', 1967},
        {'PIKE', 'ADA', 'IDL', 1992},
        {'PIKE', 'ADA', 'FANCY'},
        {'PIKE', 'CUDA', 2010},
        {'PIKE', 'CUDA', 1999},
        {'NIT', 'ADA'},
        {'NIT', 'CUDA', 2010},
        {'NIT', 'CUDA', 1999}
    )

    s1 = set(x)
    s2 = [i for i in range(len(table)) if not (len(table[i] - s1))][0]

    return s2

print(
    main(['PIKE', 'ADA', 'XSLT', 2010, 1967]),
    main(['NIT', 'CUDA', 'XSLT', 1999, 1992]),
    main(['NIT', 'ADA', 'FANCY', 1999, 1970]),
    main(['PIKE', 'ADA', 'FANCY', 2010, 1970]),
    main(['PIKE', 'CUDA', 'XSLT', 1999, 1967]),
    sep='\n'
)
