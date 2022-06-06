class RandomizedCollection:

    def __init__(self):
        self.lookup = defaultdict(set)
        self.nums = []

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.lookup[val].add(len(self.nums) - 1)
        return len(self.lookup[val]) == 1

    def remove(self, val: int) -> bool:
        res = len(self.lookup[val]) > 0
        if res:
            last = self.nums[-1]
            index = self.lookup[val].pop()
            self.nums[index] = last
            self.nums.pop()
            if self.lookup[last]:
                self.lookup[last].discard(len(self.nums))
                self.lookup[last].add(index)
        return res
            

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()