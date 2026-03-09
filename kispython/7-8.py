# Задача 7. Вычисление дерева решений
# Способ 1/4

def ada_branch(x):
    if x[2] == 'XSLT':
        return 0
    if x[2] == 'FANCY':
        return 4
    if x[2] == 'IDL':
        return {1970: 1, 1967: 2, 1992: 3}[x[4]]


def cuda_branch(x):
    return {2010: 5, 1999: 6}[x[3]]


def nit_branch(x):
    if x[1] == 'ADA':
        return 7
    if x[1] == 'CUDA':
        return {2010: 8, 1999: 9}[x[3]]


def main(x):
    table = {
        ('PIKE', 'ADA'): ada_branch,
        ('PIKE', 'CUDA'): cuda_branch,
        ('NIT', 'ADA'): lambda x: 7,
        ('NIT', 'CUDA'): lambda x: {2010: 8, 1999: 9}[x[3]],
    }

    return table[(x[0], x[1])](x)
print(
    main(['PIKE', 'ADA', 'XSLT', 2010, 1967]),
    main(['NIT', 'CUDA', 'XSLT', 1999, 1992]),
    main(['NIT', 'ADA', 'FANCY', 1999, 1970]),
    main(['PIKE', 'ADA', 'FANCY', 2010, 1970]),
    main(['PIKE', 'CUDA', 'XSLT', 1999, 1967]),
    sep='\n'
)
