class SparseVector:
    def __init__(self, nums):
        self.Dict = {}
        for idx, val in enumerate(nums):
            if val != 0:
                self.Dict[idx] = val
        print(self.Dict)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        for key in self.Dict:
            if key in vec.Dict:
                res = res + self.Dict[key]*vec.Dict[key]
        return res
nums1 = [0,1,0,0,0]; nums2 = [0,0,0,0,2]
nums1 = [0,1,0,0,2,0,0]; nums2 = [1,0,0,0,3,0,4]
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
print(v1.dotProduct(v2))
