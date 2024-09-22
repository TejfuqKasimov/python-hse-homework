"""https://leetcode.com/problems/regular-expression-matching/submissions"""

"""НА LEETCODE ТЕСТЫ КАКИЕ-ТО ТУПЫЕ НА ЭТУ ЗАДАЧУ, НО Я ГОТОВ РИСКНУТЬ"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p += "#" * max(len(s) - len(p), 0)
        # print(p)
        v = []
        flag = False

        for i in p:
            if i == "." or i == "*":
                flag = False
                v.append(i)
            else:
                if flag:
                    v[-1] += i
                else:
                    v.append(i)
                    flag = True
        ans = "true"
        count1 = 0
        for i in range(len(v)):
            if v[i] == ".":
                count1 += 1
            elif v[i] == "*":
                if len(s[count1:]) == 0 or i + 1 == len(v):
                    break
                temp = s[count1:].find(v[i + 1])
                if temp != -1:
                    count1 += temp
                else:
                    break
            elif v[i] != s[count1 : count1 + len(v[i])]:
                ans = "false"
                break

            return ans
