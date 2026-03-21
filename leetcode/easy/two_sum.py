# 1. Two Sum
# Easy

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Для каждого элемента списка проверяем, не даёт ли он в сумме с
        # другим элементом искомое число, в случае успеха возвращаем индексы
        # найденных элементов
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []

if __name__ == "__main__":
    sol = Solution()
    print(
        sol.twoSum([2, 7, 11, 15], 9),
        sol.twoSum([3, 2, 4], 6),
        sol.twoSum([3, 3], 6),
        sep="\n"
    )
