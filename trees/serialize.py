class Codec:
    null_char = 'X'

    def serialize(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ''
        serialized = ''
        to_process = [root]
        while len(to_process) > 0:
            current = to_process.pop()
            if current == None:
                serialized += self.null_char
            else:
                serialized += str(current.val)
                to_process.insert(0, current.left)
                to_process.insert(0, current.right)
            serialized += ','
        #print(serialized)
        return serialized
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        nodes = data.split(',')[:-1]
        root = TreeNode(int(nodes.pop(0)))
        current_level = [root]
        while len(nodes) > 0:
            next_level = []
            next_level_nodes = []
            next_level_size = sum(x is not None for x in current_level) * 2
            #print(f"Nodes:{nodes}, current level:{current_level}, next size:{next_level_size}")
            while next_level_size > 0:
                next_level.append(nodes.pop(0))
                next_level_size -= 1
            while len(current_level) != 0:
                current = current_level.pop(0)

                if current != None:
                    #print(f"Current:{current.val}, left:{current_level}, next_level:{next_level}")
                    left_value = next_level.pop(0)
                    left_node = self.process_value(left_value)
                    next_level_nodes.append(left_node)

                    right_value = next_level.pop(0)
                    right_node = self.process_value(right_value)
                    next_level_nodes.append(right_node)

                    current.left = left_node
                    current.right = right_node
            current_level = next_level_nodes
        return root

    def process_value(self, value) -> TreeNode:
        if value == self.null_char:
            return None
        return TreeNode(int(value))

