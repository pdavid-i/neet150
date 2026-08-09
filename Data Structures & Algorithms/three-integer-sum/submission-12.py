class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums.sort()
        print(nums)
        for i in range(len(nums)-2):
            print(' we try '+str(i))
            if (i > 0 and nums[i] == nums[i-1]):
                print('skip')
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] < -nums[i]:
                    left+=1
                elif nums[left] + nums[right] > -nums[i]:
                    right-=1
                else:
                    print('foUND')
                    solution.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while (left < right and nums[left] == nums[left-1]):
                        left+=1
                    while (right > left and nums[right] == nums[right+1]):
                        right-=1
        return solution