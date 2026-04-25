# Задача 7. Вычисление дерева решений
# Способ нерабочий

def main(x):
    if x[0] == 'PIKE' and x[1] == 'ADA':
        match(x[2]):
            case 'XSLT':
                return 0
            case 'FANCY':
                return 4
            case 'IDL':
                return {1970: 1, 1967: 2, 1992: 3}[x[4]]

    if x[0] == 'PIKE' and x[1] == 'CUDA':
        return {2010: 5, 1999: 6}[x[3]]

    if x[0] == 'NIT' and x[1] == 'ADA':
        return 7

    if x[0] == 'NIT' and x[1] == 'CUDA':
        return {2010: 8, 1999: 9}[x[3]]


print(
    main(['PIKE', 'ADA', 'XSLT', 2010, 1967]),
    main(['NIT', 'CUDA', 'XSLT', 1999, 1992]),
    main(['NIT', 'ADA', 'FANCY', 1999, 1970]),
    main(['PIKE', 'ADA', 'FANCY', 2010, 1970]),
    main(['PIKE', 'CUDA', 'XSLT', 1999, 1967]),
    sep='\n'
)
