class Solution:
    def trap(self, height: List[int]) -> int:
        num = len(height)-1
        trapped = 0
        high_left = [-1] * num
        high_right = [-1] * num

        max_left = height[0]
        for i in range(1, num):
            high_left[i] = max_left
            max_left = max(max_left, height[i])

        max_right = height[num]
        for i in range(num-1, 0, -1):
            high_right[i] = max_right
            max_right = max(max_right, height[i])

        for i in range(num):
            trap = min(high_left[i], high_right[i]) - height[i]
            if trap > 0:
                trapped += trap

        return trapped