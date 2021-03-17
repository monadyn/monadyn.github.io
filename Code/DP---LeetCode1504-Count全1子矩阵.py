from pprint import pprint
def numSubmat(mat):
        pprint(mat)
        m,n = len(mat),len(mat[0])
        partial_sum = [[0]*n for _ in range(m+1)]; #pprint(partial_sum)
        for i in range(n):#col
            tmp = 0
            for j in range(1,m+1):#row
                if mat[j-1][i] == 1:
                    tmp += 1
                partial_sum[j][i] = tmp #建表
        print('=>');pprint(partial_sum)
        def cal(row):#将二维问题转化为1维vector的情况做，排列组合，有序的1
            i = 0
            count = 0
            total_count = 0
            for num in row:
                if num==1:
                    count += 1
                else:
                    if count==1:
                        total_count += 1
                    if count>1:
                        total_count += (count+1)*count/2
                    count = 0
            if count:
                if count==1:
                    total_count += 1
                else:
                    total_count += (count+1)*count/2
            return int(total_count)
                    
        count = 0
        for top in range(m):
            for bottom in range(top+1,m+1):
                tmp_row = [0]*n
                for k in range(n):
                    if partial_sum[bottom][k]-partial_sum[top][k] == bottom-top:
                        tmp_row[k] = 1
                print(top,bottom,  tmp_row, cal(tmp_row))
                count += cal(tmp_row)
        return count

mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
mat = [[0,1,1,0],
              [0,1,1,1],
              [0,1,1,1],
              [0,1,0,1],
              [1,0,1,0],
              [1,1,1,0]]
print(numSubmat(mat))
