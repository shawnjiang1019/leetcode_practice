class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k: int) -> int:
        # use prefix product array
        if k >= len(self.prefix):
            return 0
        lower = self.prefix[-1]
        upper = self.prefix[-k - 1]
        
        return lower // upper
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)