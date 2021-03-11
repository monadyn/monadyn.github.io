from pprint import pprint
import collections

def first_missing_positive(nums):
        bit = 0
        for n in nums:
            if n > 0:
                bit |= 1 << (n - 1)
                print(bin(bit))
        flag = 0
        while bit != 0:
            if (bit & 1 == 0): #找第一个0
                print(flag, bin(bit))
                break
            flag += 1
            bit >>= 1
        print('flag', flag)
        return flag + 1    


nums = [-6, 3, 10, 14, 17, 6, 14, 1, -5, -8, 8, 15, 17, -10, 2, 7, 11, 2, 7, 11]
assert 2 == first_missing_positive([1,4,3,6,5])
