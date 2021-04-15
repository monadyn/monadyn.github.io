def reconstructQueue(people):
        people.sort(key=lambda x: x[0]) 
        ans=[-1]*len(people)
        print(ans, people)
        for i in people:
            count=i[1]
            print(i, ans)
            for j in range(len(ans)):
                if count==0 and ans[j]==-1:
                    ans[j]=i
                    break
                elif ans[j]==-1 and count!=0:
                    print('\t2: j=',j,'count=',count)
                    count-=1 
                elif i[0]<=ans[j][0]:
                    print('\t3: j=',j,'count=',count)
                    count-=1 
        return ans
print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
