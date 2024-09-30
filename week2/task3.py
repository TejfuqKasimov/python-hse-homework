"""https://leetcode.com/problems/generate-parentheses/description/"""


class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        def dfs(leftP, rightP, t):
            if leftP > n or rightP > n or leftP < rightP:
                return
            if leftP == n and rightP == n:
                ans.append(t)
                return
            dfs(leftP + 1, rightP, t + "(")
            dfs(leftP, rightP + 1, t + ")")

        ans = []
        dfs(0, 0, "")
        return ans
