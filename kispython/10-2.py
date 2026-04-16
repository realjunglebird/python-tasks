# Задача 10. Реализовать функцию для обработки табличных данных
# Способ 2 - функциональное программирование: функции map и filter,
# распаковка вместо оператора индексирования, отсутствие условных операторов и проч.

def main(original_table):
    result = list(
        map(
            lambda row: (
                lambda c1, c2, c3: [
                    c1 and c1.split(';', 1)[0].split('[', 1)[0],
                    c2 and str(c2 == 'да').lower(),
                    c3 and f"{float(c3.rstrip('%')) / 100:.2f}",
                    c1 and (
                        lambda name: f"{name.split()[1]} {name.split()[0][0]}."
                    )(c1.split(';', 1)[1])
                ]
            )(row[0], row[1], row[2]),
            dict.fromkeys(map(tuple, original_table))
        )
    )

    [print(row) for row in result]
    print()
    return result

main([
    ['sozurov7[at]rambler.ru;А.И. Соцуров', 'нет', '29%'],
    ['sozurov7[at]rambler.ru;А.И. Соцуров', 'нет', '29%'],
    ['sozurov7[at]rambler.ru;А.И. Соцуров', 'нет', '29%'],
    ['sosberg72[at]yandex.ru;Э.Ш. Сосберг', 'нет', '22%'],
    ['kofafuk3[at]yandex.ru;Д.У. Кофафук', 'нет', '66%']
])
main([
    ['fitazij22[at]yahoo.com;К.З. Фитазий', 'да', '29%'],
    ['fitazij22[at]yahoo.com;К.З. Фитазий', 'да', '29%'],
    ['fitazij22[at]yahoo.com;К.З. Фитазий', 'да', '29%'],
    ['zukidli85[at]yandex.ru;С.Ч. Цукидли', 'нет', '73%'],
    ['somizanz5[at]gmail.com;Е.С. Сомизянц', 'нет', '88%'],
    ['mebev13[at]yahoo.com;С.В. Мебев', 'нет', '23%'],
])
main([
    ['kocev60[at]gmail.com;Т.Л. Кочев', 'нет', '86%'],
    ['kezak79[at]rambler.ru;К.Г. Кецяк', 'нет', '52%'],
    ['kocev60[at]gmail.com;Т.Л. Кочев', 'нет', '86%'],
    ['zovli25[at]yahoo.com;Р.К. Зовли', 'да', '50%'],
    ['kocev60[at]gmail.com;Т.Л. Кочев', 'нет', '86%']
])
