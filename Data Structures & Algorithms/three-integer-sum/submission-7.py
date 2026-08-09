class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        for i,v in enumerate(nums):
            left = 0 
            right = len(nums) - 1
            while left <= right:
                if nums[left] + nums[right] > -v:
                    right -= 1
                elif nums[left] + nums[right] < -v:
                    left += 1
                else:
                    if left != i and right != i and left != right:      
                        candidate = sorted([nums[left], v, nums[right]])
                        if candidate not in solution:
                            solution.append(candidate)
                    left += 1
        return solution 