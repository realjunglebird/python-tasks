# 74. Search a 2D Matrix
# Medium

from tkinter.constants import X
from typing import List
import bisect


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])

        for line in matrix:
            if target not in range(line[0], line[-1]+1): continue
            i = bisect.bisect_left(line, target)
            return i < n and line[i] == target

        return False


if __name__ == "__main__":
    sol = Solution()
    print(
        sol.searchMatrix(
            matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]],
            target=3
        ),
        sol.searchMatrix(
            matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]],
            target=13
        ),
        sol.searchMatrix(
            matrix=[[1]],
            target=0
        ),
        sol.searchMatrix(
            matrix=[[1]],
            target=1
        ),
        sep="\n"
    )
