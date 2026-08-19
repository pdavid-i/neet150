class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]
        while left < right:
            mid = (left + right) // 2
            print(f"left:{left} right:{right} mid:{mid}")
            if nums[left] > nums[left + 1]:
                return nums[left + 1]
            if nums[right] < nums[right - 1]:
                return nums[right]
            if nums[left] <= nums[mid]:
                left = mid
            else:
                right = mid
        return nums[left]
