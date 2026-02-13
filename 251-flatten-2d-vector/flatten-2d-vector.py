class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.pointer = 0
        self.vector = []
        for v in vec:
            for elem in v:
                self.vector.append(elem)

    def next(self) -> int:
        res = self.vector[self.pointer]
        self.pointer += 1
        return res

    def hasNext(self) -> bool:
        if self.pointer + 1 > len(self.vector):
            return False
        return True
        


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()