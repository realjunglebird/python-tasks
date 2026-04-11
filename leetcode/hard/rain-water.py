# 42. Trapping Rain Water
# Hard

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0                # текущая позиция слева
        right = len(height) - 1 # текущая позиция справа

        left_max = 0    # максимальная стенка слева
        right_max = 0   # максимальная стенка справа

        total_water = 0 # общее количество воды

        # Двигаемся с обоих краёв к центру, запоминая наибольшие стены
        # с обеих сторон.
        while left < right:
            # Проверяем, не нашли ли ещё бОльшую стену
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # Если высота ограничена левой (меньшей) стеной
            if left_max < right_max:
                # Вычитаем из ограничения высоту, занятую текущей стеной
                total_water += left_max - height[left]
                left += 1   # Продвигаем левую позицию вперёд
            # В противном случае делаем аналогичные действия с правой стороной
            # (если макс стены равны, нам без разницы с какой стороной работать)
            else:
                total_water += right_max - height[right]
                right -= 1  # Продвигаем правую позицию вперёд

        return total_water

if __name__ == "__main__":
    sol = Solution()
    print(
        sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]),
        sol.trap([4,2,0,3,2,5]),
        sep="\n"
    )
