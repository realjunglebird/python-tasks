# Задача 9. Парсинг строки
# Способ 1

import re


def main(s):
    pattern = r'val\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*::=\s*(-?\d+)'
    matches = re.findall(pattern, s)

    result = {name: int(value) for name, value in matches}

    return result


print(
    main(r'<section> val bebiin ::= 6431 val zatige_768 ::=-6451 val onusin_219::= 1049</section>'),
    main(r'<section> val lele::= 3342 val rilece_808 ::= 8591 val zaabe::=4893</section>'),
    sep='\n'
)
