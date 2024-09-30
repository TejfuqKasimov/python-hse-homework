"""https://leetcode.com/problems/integer-to-roman/description/"""


class Solution:
    def intToRoman(self, num: int) -> str:
        alph = (
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        )
        number = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        ans = ""
        for a, n in zip(alph, number):
            while num >= n:
                num -= n
                ans += a
        return ans
