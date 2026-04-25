# Задача 8. Декодирование битового поля
# Способ 1

def main(s: str):
    x = int(s, 16)

    fields = [
        (2, 7),
        (9, 3),
        (12, 8),
        (20, 8),
        (28, 3),
    ]

    def extract(value, offset, length):
        return (value >> offset) & ((1 << length) - 1)

    return tuple(extract(x, off, ln) for off, ln in fields)


print(
    main('0x563a931b'),
    main('0x42c9e949'),
    main('0x5ba87a22'),
    main('0x70070'),
    sep='\n'
)
