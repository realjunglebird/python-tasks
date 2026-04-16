# Задача 9. Парсинг строки
# Способ 2 - разбор текста вручную: циклы, срезы, оператор индексирования.

def main(s):
    content = s.strip()
    if content.startswith('<section>'):
        content = content[8:]
    if content.endswith('</section>'):
        content = content[:-10]

    parts = [part.strip() for part in content.split('val') if part.strip()]

    result = {}
    for part in parts:
        if '::=' in part:
            name, value_str = part.split('::=', 1)
            name = name.strip()
            value = int(value_str.strip())
            result[name] = value

    return result


print(
    main(r'<section> val bebiin ::= 6431 val zatige_768 ::=-6451 val onusin_219::= 1049</section>'),
    main(r'<section> val lele::= 3342 val rilece_808 ::= 8591 val zaabe::=4893</section>'),
    sep='\n'
)
