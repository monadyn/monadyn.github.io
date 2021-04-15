from collections import deque
def maxResult(nums, k):
        #dp
        print(nums)
        queue = deque()#queue头放目前窗口内最大的
        queue.append((0,nums[0]))
        for i in range(1, len(nums)):
            print(i)
            print('\t', nums)
            cur_item = nums[i]
            #当前item，剔除k个窗口之前的大值
            if queue and queue[0][0]+k < i:
                queue.popleft()
            print('\t',queue)
            #dp[i] be "the maximum score to reach the end starting at index i".
            nums[i] += queue[0][1]
            ##丢掉q中所有小于=cur_item的item，大于cur_item的都在左边
            print('\t', nums)
            while(queue and cur_item >= queue[-1][1]):
                queue.pop()
            queue.append((i, nums[i]))
            print('\t',queue)

        return nums[-1]
def maxResult_(nums, k):
        q = deque()
        res = 0
        l = 0 # left point
        for r in range(len(nums)):
            print(l,r,nums[r], q)
            cur_item = nums[r]
            #丢掉q中所有小于cur_item的item，大于cur_item的都在左边
            while q and q[-1][1] < cur_item: q.pop()
            #cur_item放到q
            q.append((r, nums[r]))
            # l出窗
            if l>q[0][0]: q.popleft()
            #print('\t',nums[r], q)
            # 下一个r出窗
            if r+1>=k: 
                print('\tadd',q[0][1],q); 
                l+=1;res+=q[0][1];
        return res

print(maxResult([1,-1,-2,4,-7,3], 2))
