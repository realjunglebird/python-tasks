# Задача 7. Вычисление дерева решений
# Способ 5

class DecisionTree:
    def __init__(self, items):
        self.items = items

    def zero(self, a, b):
        if self.items[0] == 'NIT':
            return a
        if self.items[0] == 'PIKE':
            return b

    def one(self, a, b):
        if self.items[1] == 'CUDA':
            return a
        if self.items[1] == 'ADA':
            return b

    def two(self, a, b, c):
        if self.items[2] == 'XSLT':
            return a
        if self.items[2] == 'IDL':
            return b
        if self.items[2] == 'FANCY':
            return c

    def three(self, a, b):
        if self.items[3] == 2010:
            return a
        if self.items[3] == 1999:
            return b

    def four(self, a, b, c):
        if self.items[4] == 1970:
            return a
        if self.items[4] == 1967:
            return b
        if self.items[4] == 1992:
            return c

    def main(self):
        return self.zero(
            self.one(
                self.three(8, 9),
                7
            ),
            self.one(
                self.three(5, 6),
                self.two(0, self.four(1, 2, 3), 4)
            )
        )


def main(items):
    tree = DecisionTree(items)
    return tree.main()

print(
    main(['PIKE', 'ADA', 'XSLT', 2010, 1967]),
    main(['NIT', 'CUDA', 'XSLT', 1999, 1992]),
    main(['NIT', 'ADA', 'FANCY', 1999, 1970]),
    main(['PIKE', 'ADA', 'FANCY', 2010, 1970]),
    main(['PIKE', 'CUDA', 'XSLT', 1999, 1967]),
    sep='\n'
)
