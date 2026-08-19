class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        left = 0
        right = len(matrix) - 1
        while left < right:
            mid = (left+right+1) // 2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                return self.bin_search(matrix[mid], target)
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        return self.bin_search(matrix[right], target)


    def bin_search(self, listt, target) -> bool:
        left = 0
        right = len(listt)-1
        while left < right:
            mid = (left+right+1) // 2
            if listt[mid] == target:
                return True
            if listt[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return listt[left] == target