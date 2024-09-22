class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            ans = "0"
        else:
            ans = ""
            flag = False
            c = 0

            for i in s:
                # print(c)
                if ord(i) >= 48 and ord(i) <= 57:
                    if i == "0":
                        if flag:
                            ans += i
                    else:
                        flag = True
                        ans += i
                elif (ord(i) == 45 or ord(i) == 43) and c == 0:
                    if len(s) == 1:
                        ans = "0"
                    elif ord(i) == 45:
                        ans += i
                    elif ord(i) != 43:
                        break
                else:
                    if ord(i) != 32 or c > 0:
                        if len(ans) == 0 or ans == "-":
                            ans = "0"
                        break
                if ord(i) != 32:
                    c += 1
        if len(ans) == 0:
            ans = "0"
        ans = int(ans)
        ans = max(ans, -(2**31))
        ans = min(ans, 2**31 - 1)

        return int(ans)
