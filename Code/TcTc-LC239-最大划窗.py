from collections import deque
import heapq
def maxSlidingWindow(nums, k):
        #Heap
        n = len(nums)
        if k >= n: return [max(nums)]
        print(nums)        
        nums = [-n for n in nums]
        print(nums)        
        
        h = nums[:k]
        print('h=', h)
        heapq.heapify(h)
        print('h=', h)
        q = deque(nums[:k], k)
        #print([list(item for _, _, item in h)])
        print('q=', q)
        msw = [None]*(n-k+1)
        for j in range(n-k):
            print(j)
            while h[0] not in q:
                print('\t\tpop<<', h)
                heapq.heappop(h)
                print('\t\tpop>>', h)
            msw[j] = -h[0]
            print('\t',msw)
            q.append(nums[k+j])
            print('\tq=', q)
            heapq.heappush(h, nums[k+j])
            print('\th=', h)
        while h[0] not in q:
            heapq.heappop(h)
        msw[n-k] = -h[0]
        return msw

def maxSlidingWindow2(nums, k):
    #放弃
        n = len(nums)
        if n * k == 0: return []
        if k == 1: return nums
        left, right = [0] * n, [0] * n
        left[0] = nums[0]
        right[n - 1] = nums[n - 1]
        
        print(nums)
        print(left, right)
        for i in range(1, n):
            print(i)
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            print('\tleft', i, left[i])
            j = n - 1 - i
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])
            print('\tright', j, right[j])
        output = []
        print(left, right)
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))
        return output

def maxSlidingWindow3(nums, k):
    #优美
        d = deque()	#建立一个双端队列
        out = []
        for i, n in enumerate(nums):	#遍历数组
            print(i,n)
            while d and nums[d[-1]] < n:	#检查到本窗口的值比当前值小，pop掉
                t = d.pop()
                print('\tpop', t)
            d += i,	#把当前值加入窗口中
            print('\t', d, '这样队列中第0位永远是最大的')
            #这样队列中第0位永远是最大的

            if d[0] == i - k:	#检查最大值是否已经不在窗口中，不在就丢掉，因为每一步都检查，所以不会漏
                t = d.popleft()	#第一个窗口看到本窗口内最后一个值的时候才能找到最大值，所以从k-1处开始记录结果
                print('\tpopleft', t)
            if i >= k - 1:
                #out += nums[d[0]]
                out.append(nums[d[0]])
                print('\t', d[0], nums[d[0]], d)
        return out
#nums = [1,3,-1,-3,5,3,6,7]; k = 3
nums = [1,3,-1,-3,2,3,6,7]; k = 3
print(maxSlidingWindow(nums, k))
