# Задача 11. Обработка матриц
# черновой но более подробный вариант, НЕ принимается сайтом тк имеет операции ввода-вывода и длинные строки кода

import numpy as np

def main(D, S, W, X):
    """
    Вычисляет значение выражения:
        || S - D^2 - (X ⊙ W)^{-1} + (W ⊙ X)^{-1} + D^T ||_F
    где ⊙ — произведение Адамара (поэлементное), а (·)^{-1} — матричное обращение.
    """
    D = np.asarray(D, dtype=float)
    S = np.asarray(S, dtype=float)
    W = np.asarray(W, dtype=float)
    X = np.asarray(X, dtype=float)

    D2 = D @ D                     # матричный квадрат
    XW = X * W                     # произведение Адамара
    inv_XW = np.linalg.inv(XW)     # обратная матрица
    WX = W * X                     # то же самое, но для наглядности
    inv_WX = np.linalg.inv(WX)

    M = S - D2 - inv_XW + inv_WX + D.T
    return np.linalg.norm(M, ord='fro')


def test():
    """Автоматическое тестирование функции main с высоким покрытием."""
    # 1. Базовый тест: единичные матрицы 3×3
    I1 = np.eye(3)
    res1 = main(I1, I1, I1, I1)
    expected1 = np.sqrt(3)   # ≈ 1.7320508075688772
    assert np.isclose(res1, expected1, rtol=1e-9), f"Единичные матрицы: {res1} != {expected1}"
    print("Тест 1 пройден (единичные матрицы).")

    # 2. Тест с нулевой матрицей D и S, X=W=I
    Z = np.zeros((3, 3))
    I1 = np.eye(3)
    res2 = main(Z, Z, I1, I1)
    # ожидаем: S - D^2 = 0, члены с X,W сокращаются, D^T=0 → норма 0
    expected2 = 0.0
    assert np.isclose(res2, expected2, atol=1e-12), f"Нулевые матрицы: {res2} != {expected2}"
    print("Тест 2 пройден (нулевые матрицы).")

    # 3. Случайные матрицы (гарантированно обратимые)
    np.random.seed(42)
    n_tests = 10
    for i in range(n_tests):
        # Генерируем случайные матрицы размером 4×4
        shape = (4, 4)
        D = np.random.rand(*shape) + 0.5   # все элементы > 0 → D обратима
        S = np.random.rand(*shape) + 0.5
        W = np.random.rand(*shape) + 0.5
        X = np.random.rand(*shape) + 0.5

        # Ожидаемый результат (упрощённое выражение)
        expected = np.linalg.norm(S - D @ D + D.T, ord='fro')
        actual = main(D, S, W, X)
        assert np.isclose(actual, expected, rtol=1e-9, atol=1e-12), \
            f"Случайный тест {i+1}: {actual} != {expected}"
    print("Тест 3 пройден (10 случайных наборов матриц).")

    # 4. Проверка, что функция возвращает скаляр, а не массив
    I2 = np.eye(2)
    res4 = main(I2, I2, I2, I2)
    assert isinstance(res4, (float, np.floating)), f"Возвращён не скаляр: {type(res4)}"
    print("Тест 4 пройден (тип возвращаемого значения).")

    print("Все тесты успешно завершены.")


if __name__ == "__main__":
    test()
