class AbcNode:
    def __init__(self, value, isWord=False):
        self.value = value
        self.children = {}
        self.isWord = isWord

class WordDictionary:
    def __init__(self):
        self.root = AbcNode('§')

    def addWord(self, word: str) -> None:
        current = self.root
        for index, char in enumerate(word):
            if char in current.children.keys():
                if index == len(word)-1:
                    current.children[char].isWord = True
            else:
                current.children[char] = AbcNode(char, index == len(word)-1)
            current = current.children[char]

    def search(self, word: str) -> bool:
        return self.search_helper(self.root, word)

    def search_helper(self, current, word):
        for index, char in enumerate(word):
            if char == '.':
                for key in current.children.keys():
                    if self.search_helper(current.children[key], word[index+1:]): 
                        return True
                return False 
            elif char not in current.children.keys():
                return False
            current = current.children[char]
        return current.isWord
