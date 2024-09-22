s = input()
numRows = int(input())
if len(s) <= numRows or numRows == 1:
    ans = s
else:
    ans = ""

    for i in range(numRows):
        for j in range(len(s)):
            if ((j + i) % (numRows * 2 - 2) == 0) or (
                (j - i) % (numRows * 2 - 2) == 0
            ):
                ans += s[j]

print(ans)
