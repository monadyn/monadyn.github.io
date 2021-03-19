def isPossibleDivide(nums, k) :
        #TC: O(M logM + Mk) M: number of distinct elements in nums
        #SC: O(M)
        #Counter is used to collection frequencies of different elements in nums 
        from collections import Counter
        counter = Counter(nums)
        print(counter, sorted(counter))

        for key in sorted(counter):
            initial = counter[key]
            print(key, initial, counter)
            if initial > 0:
                for i in range(key, key+k):
                    if counter[i] < initial:
                        return False
                    counter[i] -= initial
        return True

nums = [3,2,1,2,3,4,3,4,5,9,10,11]; k = 3
nums = [3,2,2,1,2,3,4,3,4,5,9,10,11]; k = 3
print(isPossibleDivide(nums, k))
