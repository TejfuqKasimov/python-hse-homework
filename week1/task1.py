"""https://leetcode.com/problems/longest-substring-without-repeating-characters"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) > 0:
            ans = 1
            v = []
            temp = -1

            for i in range(130):
                v.append(-1)
            for i in range(len(s)):
                if v[ord(s[i])] != -1 and v[ord(s[i])] >= temp:
                    temp = v[ord(s[i])]
                v[ord(s[i])] = i
                ans = max(ans, i - temp)
                # print(v[97:123])
                # print(ans)

        else:
            ans = 0

        return ans
