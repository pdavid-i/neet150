class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count_left = self.countNodes(root.left)
        count_right = self.countNodes(root.right)

        if k <= count_left:
            return self.kthSmallest(root.left, k)
        if k == count_left+1:
            return root.val
        return self.kthSmallest(root.right, k-count_left-1)
    
    def countNodes(self, root):
        if root != None:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        return 0