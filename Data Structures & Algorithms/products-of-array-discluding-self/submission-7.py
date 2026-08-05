class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        to_return = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix[i] = product
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            postfix[i] = product
        for i in range(len(nums)):
            if i == 0:
                to_return[0] = postfix[1]
            elif i == len(nums)-1:
                to_return[i] = prefix[-2]
            else:
                to_return[i] = prefix[i-1] * postfix[i+1]
        return to_return


        