class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        for digit in num1:
            n1 = n1*10 + ord(digit) - 48 # 48 = ord('0')

        n2 = 0
        for digit in num2:
            n2 = n2*10 + ord(digit) - 48

        print(n1, n2)

        return str(n1*n2)

if __name__ == "__main__":
    sol = Solution()
    print(
        sol.multiply("2", "3"),
        sol.multiply("123", "456")
    )
