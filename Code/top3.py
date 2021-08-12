
def top3_a(nums): #plan a
    n = len(nums)
    if n <=3: return nums

#nums=[1,2,3,4,5,6]
    res = [0]*3
    
    res[0] =nums[0]
    res[1] =nums[1]
    res[2] =nums[2]
    res = sorted(res[:3], reverse=True) #klog(k)
    res.append(0)
    print('res=', res)
#res=[3,2,1]
# cur=4
#res=[4,3,2]

    for i in range(3,n):
        print('+', i, res)
        cur = nums[i]
        j = 2
        while j>=0: #O(k) -> Olog(k)(heap/binary_search)
            tmp = res[j]
            if cur > res[j]:  
                res[j] = cur
                res[j+1] = tmp
            j -= 1
        print('-', i, res)
    return res[:3] #Onlog(k)

import heapq
def top3(nums,k): #plan b
    n = len(nums)
    res = nums[:k]
    heapq.heapify(res) #Oklog(k)
    print('res=', res)
    for i in range(k, n):
        cur = nums[i]
        if cur > res[0]:#Olog(k)
            heapq.heappushpop(res, cur)
        print(cur, res)
    return res



nums=[1,2,3,4,5,6,7,8,9,10,11,12,13]
print(top3(nums, 5))

