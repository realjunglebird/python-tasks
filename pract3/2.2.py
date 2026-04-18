import numpy as np
import matplotlib.pyplot as plt

def generate_sprite():
    # Создаём пустую сетку 5x5
    # Используем 3 столбца для генерации (2 боковых + 1 центральный)
    left_side = np.random.randint(0, 2, (5, 3))

    # Зеркально отражаем первые 2 столбца, чтобы получить правую сторону
    # Индексация [:, 1::-1] берёт 1-й и 0-й столбцы
    right_side = left_side[:, :2][:, ::-1]

    # Соединяем левую часть (вместе с центром) и правую часть
    sprite = np.hstack((left_side, right_side))

    return sprite

def generate_sprite_map(rows=10, cols=20, padding=2):
    """Создаёт сетку спрайтов с заданными отступами."""
    sprite_size = 5

    # Вычисляем размер общего холста
    total_h = rows * (sprite_size + padding)
    total_w = cols * (sprite_size + padding)

    # Создаём чёрный холст
    sprite_map = np.zeros((total_h, total_w))

    for r in range(rows):
        for c in range(cols):
            sprite = generate_sprite()

            # Вычисляем координаты вставки для текущего спрайта
            start_y = r * (sprite_size + padding)
            start_x = c * (sprite_size + padding)

            # Помещаем спрайт в сетку
            sprite_map[
                start_y: start_y + sprite_size,
                start_x: start_x + sprite_size
            ] = sprite
    
    return sprite_map

# Параметры генерации
rows, cols = 10, 20
sprite_sheet = generate_sprite_map(rows, cols, padding=5)

# Визуализация
plt.figure(figsize=(12, 6))
plt.imshow(sprite_sheet, cmap='gray', interpolation='nearest')
plt.axis('on')
plt.tight_layout()
plt.show()
