class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stacks = [[nums.pop(-1), 1]]
        for i, num in enumerate(nums[::-1]):
            used = False
            new_candidates = []
            # optimization - might be worth or nah
            worth_new = max(stack[1] for stack in stacks) < (len(nums) - i) 
            for stack in stacks:
                if num < stack[0]:
                    # give a chance to seq not taking it into acc
                    if worth_new:
                        new_candidates.append([stack[0],stack[1]])
                    stack[0] = num
                    stack[1] += 1
                if num == stack[0]:
                    used = True
            if not used and worth_new:
                stacks.append([num, 1])
            if len(new_candidates):
                stacks.extend(new_candidates)
            filtered = {}
            for stack in stacks:
                if stack[0] in filtered:
                    if filtered[stack[0]] < stack[1]:
                        filtered[stack[0]] = stack[1]
                else:
                    filtered[stack[0]] = stack[1]
            stacks = [[key, filtered[key]] for key in filtered]
        return max(stack[1] for stack in stacks)