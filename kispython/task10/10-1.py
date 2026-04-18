# Задача 10. Реализовать функцию для обработки табличных данных
# Способ 1 - императивное решение с циклами, списками, условными операторами.

class Table:
    def __init__(self, table):
        self.table = table

    def remove_duplicates(self):
        seen = {}
        uniques = []
        for i in range(len(self.table)):
            row = tuple(self.table[i])
            if row not in seen:
                seen[row] = i
                uniques.append(i)
        self.table = [self.table[j] for j in uniques]

    def split_column(self):
        new_table = []
        for row in self.table:
            if row[0] is not None:
                parts = row[0].split(';', 1)
                email = parts[0]
                name = parts[1]
                new_row = [email, name] + row[1:]
                new_table.append(new_row)
            else:
                new_row = [None, None] + row[1:]
                new_table.append(new_row)
        self.table = new_table

    def convert_email(self, cell):
        if cell is not None:
            return cell.split('[')[0]

    def convert_status(self, cell):
        return 'true' if cell == 'да' else 'false'

    def convert_percentage(self, cell):
        return format(int(cell[:-1]) / 100, '.2f')

    def convert_name(self, cell):
        name_parts = cell.split()
        return f"{name_parts[1]} {name_parts[0][:-2]}"

    def convert_table(self):
        new_table = []
        for row in self.table:
            email = self.convert_email(row[0])
            status = self.convert_status(row[2])
            percentage = self.convert_percentage(row[3])
            name = self.convert_name(row[1])
            new_table.append([email, status, percentage, name])
        self.table = new_table

    def get(self):
        return self.table

    def print(self):
        for row in self.table:
            print(row)
        print('\n')


def main(original_table):
    table = Table(original_table)
    table.remove_duplicates()
    table.split_column()
    table.convert_table()
    table.print()
    return table.get()



main([
    ["sozurov7[at]rambler.ru;А.И. Соцуров", "нет", "29%"],
    ["sozurov7[at]rambler.ru;А.И. Соцуров", "нет", "29%"],
    ["sozurov7[at]rambler.ru;А.И. Соцуров", "нет", "29%"],
    ["sosberg72[at]yandex.ru;Э.Ш. Сосберг", "нет", "22%"],
    ["kofafuk3[at]yandex.ru;Д.У. Кофафук", "нет", "66%"],
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
