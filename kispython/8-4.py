# Задача 8. Декодирование битового поля
# Способ 2

def main(s):
    bits = f'{int(s, 16):032b}'

    v2 = int(bits[32-9:32-2], 2)
    v3 = int(bits[32-12:32-9], 2)
    v4 = int(bits[32-20:32-12], 2)
    v5 = int(bits[32-28:32-20], 2)
    v6 = int(bits[32-31:32-28], 2)

    return (v2, v3, v4, v5, v6)

print(
    main('0x563a931b'),
    main('0x42c9e949'),
    main('0x5ba87a22'),
    main('0x70070'),
    sep='\n'
)
