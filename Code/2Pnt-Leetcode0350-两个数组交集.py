import collections
def solution1(nums1, nums2):
    print(collections.Counter(nums1))
    print(collections.Counter(nums2))
    print(collections.Counter(nums1) & collections.Counter(nums2))
    return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())
def solution(nums1, nums2):
        res = []
        nums1.sort()
        nums2.sort()
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1

        return res

nums1 = [1, 2, 2, 1]
nums2 = [2, 2, 3, 2]
print(solution(nums1, nums2))
