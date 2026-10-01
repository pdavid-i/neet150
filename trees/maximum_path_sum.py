# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def bobo(root: Optional[TreeNode]) -> int:
    maxim = -999999
    def helper(root):
        nonlocal maxim
        if root.left == None and root.right == None:
            return root.val
        left_score = right_score = -999999999
        if root.left != None:
            left_score = helper(root.left)
        if root.right != None:
            right_score = helper(root.right)
        top = max(root.val, root.val+left_score, root.val+right_score, root.val+left_score)
        maxim = max(maxim, top, right_score, left_score, root.val+left_score+right_score)
        return top
    top = helper(root)
    return max(top, maxim)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return bobo(root)