class Solution:
    def maxDepth(self, root):
        if root:
            return max(1 + self.maxDepth(root.right), 1 + self.maxDepth(root.left))
        return 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            right = self.maxDepth(root.right)
            left = self.maxDepth(root.left)
            return max(
                right + left,
                self.diameterOfBinaryTree(root.left),
                self.diameterOfBinaryTree(root.right),
            )
        return 0
