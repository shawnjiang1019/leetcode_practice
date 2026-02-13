class FileSharing:

    def __init__(self, m: int):
        # keep a hashmap chunk: users pair
        self.ids = set()
        self.chunks = {}
        for i in range(1, m + 1):
            self.chunks[i] = set()
        self.users = {}
        
        

    def join(self, ownedChunks: List[int]) -> int:
        # find the valid ID.
        i = 1
        while i in self.ids:
            i += 1
        for chunk in ownedChunks:
            self.chunks[chunk].add(i)
        self.users[i] = set(ownedChunks)
        self.ids.add(i)
        return i

    def leave(self, userID: int) -> None:
        for chunk in self.users[userID]:
            self.chunks[chunk].remove(userID)
        self.users.pop(userID)
        self.ids.remove(userID)

    def request(self, userID: int, chunkID: int) -> List[int]:
        owners = sorted(self.chunks[chunkID])
        if owners:
            self.chunks[chunkID].add(userID)
            if chunkID not in self.users[userID]:
                self.users[userID].add(chunkID)
        return owners


# Your FileSharing object will be instantiated and called as such:
# obj = FileSharing(m)
# param_1 = obj.join(ownedChunks)
# obj.leave(userID)
# param_3 = obj.request(userID,chunkID)