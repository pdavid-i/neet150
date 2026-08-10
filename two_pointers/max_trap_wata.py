class Solution:
    def trap(self, height: List[int]) -> int:
        num = len(height) - 1
        trapped = 0
        high_left = [-1] * num
        high_right = [-1] * num

        max_left = height[0]
        for i in range(1, num):
            high_left[i] = max_left
            max_left = max(max_left, height[i])

        max_right = height[num]
        for i in range(num - 1, 0, -1):
            high_right[i] = max_right
            max_right = max(max_right, height[i])

        for i in range(num):
            trap = min(high_left[i], high_right[i]) - height[i]
            if trap > 0:
                trapped += trap

        return trapped

class Solution2:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left = 0
        right = len(height) - 1
        wata = 0
        while height[left + 1] > height[left]:
            left += 1
        while height[right - 1] > height[right]:
            right -= 1
        left_max = height[left]
        right_max = height[right]
        while left < right:
            if left_max < right_max:
                left += 1
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    wata += min(left_max, right_max) - height[left]
            else:
                right -= 1
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    wata += min(left_max, right_max) - height[right]
        return wata
