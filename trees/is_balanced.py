class Solution:
    def maxDepth(self, root):
        if root:
            return max(1 + self.maxDepth(root.right), 1 + self.maxDepth(root.left))
        return 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            rootBalanced = (
                abs(self.maxDepth(root.left) - self.maxDepth(root.right)) <= 1
            )
            return (
                rootBalanced
                and self.isBalanced(root.left)
                and self.isBalanced(root.right)
            )
        return True
