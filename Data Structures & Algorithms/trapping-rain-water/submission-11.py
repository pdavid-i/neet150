class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        left = 0 
        right = len(height) - 1
        wata = 0
        while height[left+1]>height[left]:
            left += 1
        while height[right-1]>height[right]:
            right -=1
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
                right -=1 
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    wata += min(left_max, right_max) - height[right]
        return wata