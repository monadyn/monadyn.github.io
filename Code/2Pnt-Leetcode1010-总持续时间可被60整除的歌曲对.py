def numPairsDivisibleBy60_1(time):
        """
        brute-force
        """
        res = 0
        for i in range(0, len(time) - 1):
            for j in range(i + 1, len(time)):
                # print time[i], time[j]
                if (time[i] + time[j]) % 60 == 0:
                    res += 1 
        return res
def numPairsDivisibleBy60_2(time):
        record = [0 for _ in range(0, 60)]
        for index, item in enumerate(time):
            record[item % 60] += 1
        print(record) 
        res = 0
        for i in range(0, 60):
            if i in [0, 30] and record[i] > 1:
                res += record[i] * (record[i] - 1) # 对于0 和 30 来说，在它们中取得所有结果的个数为C N 2 = N *(N - 1) / 2， N是自身统计的个数
                record[i] = 0 # 一次处理完所有的这样的数，然后把record[0]归零，保证不重复计算
            elif i:            
                res += record[60 - i] * record[i]
        return res // 2

        #for i in range(0, len(time)):
        #    temp = time[i] % 60
 
        #    if temp:
        #        record[temp] -= 1
        #        res += record[60 - temp]
        #    elif temp == 0 and record[0] > 1:
        #        # print res, record[0]
        #        # 5 4+3 +2 +1
        #        res += record[0] * (record[0] - 1) // 2
        #        record[0] = 0 
        return res
times = [30,20,150,100,40]
#print(numPairsDivisibleBy60_1(times))
print(numPairsDivisibleBy60_2(times))
