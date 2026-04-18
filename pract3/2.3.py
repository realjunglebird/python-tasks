import numpy as np
import matplotlib.pyplot as plt

# Подготовка палитры PICO-8
palette_hex = [
    "1D2B53",
    "7E2553",
    "008751",
    "AB5236",
    "5F574F",
    "C2C3C7",
    "FFF1E8",
    "FF004D",
    "FFA300",
    "FFEC27",
    "00E436",
    "29ADFF",
    "83769C",
    "FF77A8",
    "FFCCAA"
]

def hex_to_rgb(hex_str):
    return [int(hex_str[i:i+2], 16) for i in (0, 2, 4)]

# Создаём массив RGB цветов
palette_rgb = [hex_to_rgb(h) for h in palette_hex]

def generate_color_sprite(n=8, m=8):
    "Генерирует симметричный цветной спрайт NxM."
    
    # Создаём пустой спрайт
    sprite = np.zeros((n, m, 3), dtype=np.uint8)

    # Случайным образом выбираем основной цвет спрайта из палитры
    main_color = palette_rgb[np.random.randint(len(palette_rgb))]

    # Таким же образом выбираем второй акцентный цвет
    accent_color = palette_rgb[np.random.randint(len(palette_rgb))]

    # Генерируем только левую половину (с учётом центрального столбца)
    half_m = (m // 2) + (m % 2)

    for r in range(n):
        for c in range(half_m):
            # Вероятность закрашивания пикселя
            if np.random.random() > 0.5:
                color = main_color if np.random.random() > 0.2 else accent_color
                sprite[r, c] = color
                sprite[r, m - 1 - c] = color
    
    return sprite

def generate_sprite_map(rows=10, cols=15, n=8, m=8, padding=2):
    "Создаёт карту цветных спрайтов."
    total_h = rows * (n + padding) + padding
    total_w = cols * (m + padding) + padding

    # Создаём чёрный холст
    sprite_map = np.zeros((total_h, total_w, 3), dtype=np.uint8)

    for r in range(rows):
        for c in range(cols):
            sprite = generate_color_sprite(n, m)
            start_y = r * (n + padding) + padding
            start_x = c * (m + padding) + padding

            sprite_map[
                start_y: start_y + n,
                start_x: start_x + m
            ] = sprite

    return sprite_map

rows, cols = 10, 18
n_size, m_size = 8, 8

final_map = generate_sprite_map(rows, cols, n_size, m_size, padding=2)

plt.figure(figsize=(14, 8), facecolor='black')
plt.imshow(final_map, interpolation='nearest')
plt.axis('on')
plt.tight_layout()
plt.show()
