class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        is_fucked = False
        multiplied_once = False
        for nr in nums:
            if nr != 0:
                product*=nr
                multiplied_once = True
            else:
                if is_fucked == True:
                    product = 0
                else:
                    is_fucked = True
                
        to_return = []
        for nr in nums:
            if nr == 0:
                if multiplied_once == True:
                    to_return.append(product)
                else:
                    to_return.append(0)
            elif is_fucked:
                to_return.append(0)
            else:
                to_return.append(int(product/nr))
        return to_return
        