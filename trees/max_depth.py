class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))
        return 0