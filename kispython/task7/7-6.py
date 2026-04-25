# Задача 7. Вычисление дерева решений
# Способ нерабочий

def main(x):
    rules = [
        lambda x: x[0] == 'PIKE' and x[1] == 'ADA' and x[2] == 'XSLT',
        lambda x: (x[0] == 'PIKE' and x[1] == 'ADA' and
                   x[2] == 'IDL' and x[4] == 1970),
        lambda x: (x[0] == 'PIKE' and x[1] == 'ADA' and
                   x[2] == 'IDL' and x[4] == 1967),
        lambda x: (x[0] == 'PIKE' and x[1] == 'ADA' and
                   x[2] == 'IDL' and x[4] == 1992),
        lambda x: x[0] == 'PIKE' and x[1] == 'ADA' and x[2] == 'FANCY',
        lambda x: x[0] == 'PIKE' and x[1] == 'CUDA' and x[3] == 2010,
        lambda x: x[0] == 'PIKE' and x[1] == 'CUDA' and x[3] == 1999,
        lambda x: x[0] == 'NIT' and x[1] == 'ADA',
        lambda x: x[0] == 'NIT' and x[1] == 'CUDA' and x[3] == 2010,
        lambda x: x[0] == 'NIT' and x[1] == 'CUDA' and x[3] == 1999,
    ]

    for i, f in enumerate(rules):
        if f(x):
            return i

print(
    main(['PIKE', 'ADA', 'XSLT', 2010, 1967]),
    main(['NIT', 'CUDA', 'XSLT', 1999, 1992]),
    main(['NIT', 'ADA', 'FANCY', 1999, 1970]),
    main(['PIKE', 'ADA', 'FANCY', 2010, 1970]),
    main(['PIKE', 'CUDA', 'XSLT', 1999, 1967]),
    sep='\n'
)
