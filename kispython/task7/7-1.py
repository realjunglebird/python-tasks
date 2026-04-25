# Задача 7. Вычисление дерева решений
# Способ нерабочий

def main(x):
    match(x[0]):
        case 'PIKE':
            match(x[1]):
                case 'ADA':
                    match(x[2]):
                        case 'XSLT':
                            return 0
                        case 'FANCY':
                            return 4
                        case 'IDL':
                            match(x[4]):
                                case 1970:
                                    return 1
                                case 1967:
                                    return 2
                                case 1992:
                                    return 3
                case 'CUDA':
                    match(x[3]):
                        case 2010:
                            return 5
                        case 1999:
                            return 6
        case 'NIT':
            match(x[1]):
                case 'ADA':
                    return 7
                case 'CUDA':
                    match(x[3]):
                        case 2010:
                            return 8
                        case 1999:
                            return 9


print(
    main(['PIKE', 'ADA', 'XSLT', 2010, 1967]),
    main(['NIT', 'CUDA', 'XSLT', 1999, 1992]),
    main(['NIT', 'ADA', 'FANCY', 1999, 1970]),
    main(['PIKE', 'ADA', 'FANCY', 2010, 1970]),
    main(['PIKE', 'CUDA', 'XSLT', 1999, 1967]),
    sep='\n'
)
