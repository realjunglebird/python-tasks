# 13. Roman to Integer
# Easy

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        # Проходимся по парам соседних символов
        for a, b in zip(s, s[1:]):
            # Если перед бОльшим числом стоит меньшее,
            # вычитаем его, в противном случае суммируем оба числа
            if roman[a] < roman[b]:
                result -= roman[a]
            else:
                result += roman[a]
        # Т.к. последний символ остался необработанным, прибавляем его к
        # результату
        return result + roman[s[-1]]

if __name__ == "__main__":
    sol = Solution()
    print(
        sol.romanToInt("III"),
        sol.romanToInt("LVIII"),
        sol.romanToInt("MCMXCIV"),
        sep="\n"
    )
