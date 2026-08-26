class Node:
    def __init__(self, value, prv=None, nxt=None):
        self.value = value
        self.prv = prv
        self.nxt = nxt

    def stringifi(self):
        return f"Value {self.value}, next: {self.nxt}, prev: {self.prv}"

    def __str__(self):
        return f"v:{self.value} p:{self.prv} n:{self.nxt}"

    def __repr__(self):
        return f"v:{self.value} p:{self.prv} n:{self.nxt}"


class LRUCache:
    def __init__(self, capacity: int):
        self.load = 0
        self.capacity = capacity
        self.tail = None
        self.head = None
        self.dic = {}

    def refreshKey(self, key):
        if key not in self.dic:
            print(f"Key {key} not in here dawg")
        if key == self.head:
            return
        next_key = self.dic[key].nxt
        prev_key = self.dic[key].prv
        # if it's in the middle update both links
        if next_key != None and prev_key != None:
            self.dic[next_key].prv = prev_key
            self.dic[prev_key].nxt = next_key
        # if it's at the back update the tail
        elif prev_key == None and self.load >= 2:
            self.tail = self.dic[self.tail].nxt
            self.dic[self.tail].prv = None
        # if it's at the front, it will be updated anyway
        self.dic[self.head].nxt = key
        self.dic[key].nxt = None
        self.dic[key].prv = self.head
        self.head = key

    def get(self, key: int) -> int:
        if key in self.dic:
            self.refreshKey(key)
            return self.dic[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].value = value
            return self.refreshKey(key)

        # print(f"put k:{key} v:{value} h:{self.head} t:{self.tail}")
        if self.load >= self.capacity:
            # print(f"big {self.load} >= {self.capacity}, dic:{self.dic}")
            # remove the oldest entry
            old_tail = self.tail
            self.tail = self.dic[self.tail].nxt
            del self.dic[old_tail]
            if self.tail != None:
                self.dic[self.tail].prv = None
            self.load -= 1

        # add a new key-value to the cache
        if self.load == 0:
            self.dic[key] = Node(value)
            self.head = self.tail = key
        else:
            self.dic[key] = Node(value, self.head, None)
            self.dic[self.head].nxt = key
            self.head = key
        self.load += 1
