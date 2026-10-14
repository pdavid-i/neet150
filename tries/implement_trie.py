class AbcNode:
    def __init__(self, value, isWord=False):
        self.value = value
        self.children = {}
        self.isWord = isWord

class PrefixTree:
    def __init__(self):
        self.root = AbcNode('§')

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char in current.children.keys():
                if char == word[-1]:
                    current.children[char].isWord = True
            else:
                current.children[char] = AbcNode(char, char == word[-1])
            current = current.children[char]

    def search(self, word: str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children.keys():
                return False
            current = current.children[char]
        return current.isWord == True


    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children.keys():
                return False
            current = current.children[char]
        return True
