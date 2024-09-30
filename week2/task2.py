"""https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/"""


class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if len(digits) == 0:
            return []
        alph = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = [""]
        for i in digits:
            s = alph[int(i) - 2]
            ans = [a + b for a in ans for b in s]
        return ans
