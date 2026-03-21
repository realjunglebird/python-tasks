#
# Easy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original_number = x
        reversed_number = 0

        # Собираем развёрнутое число, находя каждую из цифр исходного числа
        # с конца с помощью остатка от деления на 10
        while x > 0:
            reversed_number *= 10
            reversed_number += x % 10
            x = x // 10

        return original_number == reversed_number

if __name__ == "__main__":
    sol = Solution()
    print(
        sol.isPalindrome(121),
        sol.isPalindrome(-121),
        sol.isPalindrome(10),
        sep="\n"
    )
