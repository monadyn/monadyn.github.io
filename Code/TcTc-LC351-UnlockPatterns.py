def numberOfPatterns(m, n):
        def backtracking(curr_key,step):
            if step == 1:
                return 1
            count = 0
            seen[curr_key] = True
            for i in range(1,10):
                # just continue is the key i has been visited
                if seen[i]:
                    continue
                #一种情况是到上下左右或者四个对角相邻的位置，另一种情况通过相邻且已经被访问过的位置到另一个不相邻的位置
                # if key i not in d[curr_key],meaning it is a beighbor of curr_key
                if i not in d[curr_key]:
                    count += backtracking(i,step-1)
                
                if i in d[curr_key] and seen[d[curr_key][i]]:
                    count += backtracking(i,step-1)
                
            seen[curr_key] = False 
            return count
        
        seen = [False]*10
        total_way = 0
        #invalid
        #非法的，首先1不能直接到3，必须经过2，同理的有4到6，7到9，1到7，2到8，3到9，还有就是对角线必须经过5，例如1到9，3到7等
        d = {1:{9:5,3:2,7:4},  2:{8:5}, 3:{1:2,9:6, 7:5} , 4:{6:5},5:{}, 6:{4:5},7:{1:4,3:5,9:8}, 8:{2:5}, 9:{7:8,1:5,3:6}}
        for step in range(m,n+1):
            for curr_key in range(1,10):
                total_way += backtracking(curr_key,step)
        
        return total_way
print(numberOfPatterns(3,5))
