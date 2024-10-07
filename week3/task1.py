"""https://leetcode.com/problems/container-with-most-water/"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointerL = 0
        pointerR = len(height) - 1
        ans = 0

        while pointerL < pointerR:
            ans = max(
                ans,
                (pointerR - pointerL)
                * min(height[pointerL], height[pointerR]),
            )
            if height[pointerR] < height[pointerL]:
                pointerR -= 1
            elif height[pointerR] > height[pointerL]:
                pointerL += 1
            else:
                pointerL += 1
                pointerR -= 1
        return ans
