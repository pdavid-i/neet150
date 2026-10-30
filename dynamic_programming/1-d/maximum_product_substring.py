class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if 0 in nums:
            idx = nums.index(0)
            lft = nums[:idx]
            rite = nums[idx+1:]
            left = right = -100
            if len(lft) > 0:
                left = self.maxProduct(lft)
            if len(rite) > 0:
                right = self.maxProduct(rite)
            return max([left, right, 0])
        maxp = minp = cmax = cmin = nums[0]
        for num in nums[1:]:
            cmaxclone = cmax
            cmax = max([num, num*cmax, num*cmin])
            cmin = min([num, num*cmin, num*cmaxclone])
            maxp = max([maxp, cmax])
            minp = min([minp, cmin])
            #print(f'After:{num}, cmax:{cmax} cmin:{cmin} Max:{maxp} Min:{minp}')

        return maxp