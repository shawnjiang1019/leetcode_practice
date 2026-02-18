class SmallestInfiniteSet:

    def __init__(self):
        self.smallest_heap = []
        self.smallest_set = set()
        for i in range(1, 1001):
            self.smallest_heap.append(i)
            self.smallest_set.add(i)
        heapq.heapify(self.smallest_heap)

    def popSmallest(self) -> int:
        res = heapq.heappop(self.smallest_heap)
        self.smallest_set.remove(res)
        return res

    def addBack(self, num: int) -> None:
        if num not in self.smallest_set:
            self.smallest_set.add(num)
            heapq.heappush(self.smallest_heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)