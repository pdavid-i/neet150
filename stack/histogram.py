class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        histogram = 0
        for height in heights:
            # measure current possible area
            if len(stack) == 0:
                histogram = max(histogram, height)
                stack.append([height, 1])
                continue
            
            # reevaluate stack with current element
            if height > stack[-1][0]:
                stack.append([height, 1])
            elif height == stack[-1][0]:
                stack[-1][1] += 1
            else:
                countem = 0
                while len(stack) > 0 and height <= stack[-1][0]:
                    popped = stack.pop()
                    histogram = max(histogram, popped[0] * (popped[1]+countem))
                    countem += popped[1] #when peak is obsolete, add the frequencies to the one that still stands
                stack.append([height, countem+1])

            histogram = max(histogram, stack[-1][0] * (stack[-1][1]))
        countt = 0
        while len(stack) > 0:
            popped = stack.pop()
            histogram = max(histogram, popped[0] * (popped[1]+countt))
            countt += popped[1]

        return histogram