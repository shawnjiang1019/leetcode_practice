class RandomizedSet:

    def __init__(self):
        self.idx = {}
        self.arr = []
        
    def insert(self, val: int) -> bool:
        if val not in self.idx:
            self.arr.append(val)
            self.idx[val] = len(self.arr) - 1
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val not in self.idx:
            return False
        val_idx = self.idx[val]
        last_element = self.arr[-1]

        self.arr[val_idx] = last_element
        self.idx[last_element] = val_idx
        
        self.arr.pop()
        self.idx.pop(val)
        return True
        
    def getRandom(self) -> int:
        random_idx = random.randint(0, len(self.arr)-1)
        return self.arr[random_idx]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()