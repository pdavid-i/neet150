class Solution:
    def __init__(self):
        self.target = ""
        self.found = False
        self.board = None
        self.width = 0
        self.height = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.target = word
        self.found = False
        self.board = board
        self.width = len(board[0])
        self.height = len(board)
        for y in range(self.height):
            for x in range(self.width):
                used = [[False for x in board[0]] for y in board]
                candidate = board[y][x]
                used[y][x] = True
                self.backtrack(candidate, used, x, y)
                if self.found:
                    return True
        return self.found

    def backtrack(self, candidate, used, x, y):
        if candidate == self.target or self.found:
            self.found = True
            return 

        # go right
        self.step(x+1, y, candidate, used)
        # go down 
        self.step(x, y+1, candidate, used)
        #go left
        self.step(x-1, y, candidate, used)
        #go up
        self.step(x, y-1, candidate, used)

    def step(self, x, y, candidate, used):
        if self.valid_move(x, y, candidate, used):
            candidate += self.board[y][x]
            used[y][x] = True
            self.backtrack(candidate, used, x, y)
            used[y][x] = False
            candidate = candidate[:-1]

    def valid_move(self, x, y, candidate, used):
        return 0 <= x < self.width and 0 <= y < self.height and not used[y][x] and self.validate(candidate+self.board[y][x])

    def validate(self, word):
        if word in self.target:
            return True
        return False
