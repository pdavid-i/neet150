class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        to_process = [root]
        level_order = [[root.val]]
        while len(to_process) != 0:
            current_level = []
            for node in to_process:
                if node.left != None:
                    current_level.append(node.left)
                if node.right != None:
                    current_level.append(node.right)
            if len(current_level) != 0:
                level_order.append([node.val for node in current_level])
            to_process = current_level
        return level_order
