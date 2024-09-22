"""https://leetcode.com/problems/longest-palindromic-substring"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        ans_s = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                temp_s = s[i : j + 1]
                if temp_s == temp_s[::-1]:
                    if ans < j - i + 1:
                        ans = j - i + 1
                        ans_s = temp_s

        return ans_s
