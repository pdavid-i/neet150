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

    def step(self, letter, node):
        if letter in node.children.keys():
            return node.children[letter]
        return None

class Solution:
    def __init__(self):
        self.words = []
        self.found = []
        self.board = None
        self.width = 0
        self.height = 0
        self.trie = None
        return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.words = words
        self.found = []
        self.board = board
        self.width = len(board[0])
        self.height = len(board)
        self.init_trie()
        for y in range(self.height):
            for x in range(self.width):
                first_node = self.trie.step(board[y][x], self.trie.root)
                if first_node != None:
                    used = [[False for x in board[0]] for y in board]
                    candidate = board[y][x]
                    used[y][x] = True
                    self.backtrack(candidate, used, x, y, first_node)
        return self.found

    def init_trie(self):
        self.trie = PrefixTree()
        for word in self.words:
            self.trie.insert(word)

    def backtrack(self, candidate, used, x, y, node):
        if self.trie.search(candidate) and candidate not in self.found:
            self.found.append(candidate)

        # go right
        self.step(x+1, y, candidate, used, node)
        # go down 
        self.step(x, y+1, candidate, used, node)
        #go left
        self.step(x-1, y, candidate, used, node)
        #go up
        self.step(x, y-1, candidate, used, node)

    def step(self, x, y, candidate, used, node):
        if self.valid_move(x, y, candidate, used):
            prev = node
            node = self.trie.step(self.board[y][x], node)
            if node != None:
                candidate += self.board[y][x]
                used[y][x] = True
                self.backtrack(candidate, used, x, y, node)
                used[y][x] = False
                candidate = candidate[:-1]
            node = prev
    
    def valid_move(self, x, y, candidate, used):
        return 0 <= x < self.width and 0 <= y < self.height and not used[y][x]