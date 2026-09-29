class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countem(root, root.val)

    def countem(self, root, maxx):
        count = 0
        if root.val >= maxx:
            count += 1
        if root.left != None:
            count += self.countem(root.left, max(root.val, maxx))
        if root.right != None:
            count += self.countem(root.right, max(root.val, maxx))
        return count
