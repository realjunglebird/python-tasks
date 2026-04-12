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

# Генерируем спрайт
sprite_data = generate_sprite()

# Визуализация
plt.figure(figsize=(4, 4))

# Используем cmap='gray' для чёрно-белого отображения (0 - чёрный, 1 - белый)
plt.imshow(sprite_data, cmap='gray', interpolation='nearest')

# Настройка осей
plt.xticks(np.arange(5))
plt.yticks(np.arange(5))

plt.show()
