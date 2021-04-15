def partitionLabels(S):
        maps = {} # store 26 chars
		# Find starting and ending index of each character
        for i in range(len(S)):
            if S[i] not in maps:
                maps[S[i]] = [i,i]
            else:
                maps[S[i]][1] = i
		# Merge Intervals
        interval = list(maps.values())
        print(interval)
        start = interval[0][0]
        end = interval[0][1]
        print(start, end)
        res = []
        for i in range(1,len(interval)):
            print(i, interval[i])
            if interval[i][0] > end:
                res.append(end-start + 1)
                start = interval[i][0]
                end = interval[i][1]
            else:
                end = max(end,interval[i][1])
        res.append(end-start + 1)
        return res
print(partitionLabels('ababcbacadefegdehijhklij'))
