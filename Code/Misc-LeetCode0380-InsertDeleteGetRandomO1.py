class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = list(), dict()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        """
        if val in self.pos:
            print(self.nums, self.pos, val)
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx] = last
            self.pos[last] = idx

            print(self.nums)
            self.nums.pop()
            print(self.nums)
            print(self.pos)
            #self.pos.pop(val, 0)
            self.pos.pop(val)
            print(self.pos)
            return True
        return False

    def getRandom(self):
        import random
        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]

randomSet = RandomizedSet()
randomSet.insert(1);
randomSet.remove(2);
randomSet.insert(2);
randomSet.insert(5);
randomSet.insert(4);
randomSet.getRandom();
randomSet.remove(1);
randomSet.insert(2);
randomSet.getRandom();
