import heapq
from pprint import pprint
def trapRainWater2(heightMap):
        #BFS
        if not heightMap or not heightMap[0]:
            return 0
			
			
		# Initial
		# Board cells cannot trap the water
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
			
        pprint(heightMap)			
		# Add Board cells first
        heap = []
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    heightMap[i][j] = -1
        pprint(heightMap)			
        pprint(heap)
					
					
		# Start from level 0
        level, res = 0, 0
        
        while heap:
            height, x, y = heapq.heappop(heap)#heapq每次取得都是最小的level
            #print('\t',height, x, y, level)
            level = max(height, level)
            print('\t',height, x, y, 'level=', level)

            for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= i < m and 0 <= j < n and heightMap[i][j] != -1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    print('\t\t+', res, heightMap[i][j], 'i,j = ',i, j, level)
					# If cell's height smaller than the level, then it can trap the rain water
                    if heightMap[i][j] < level:
                        res += level - heightMap[i][j]
                    print('\t\t-', res)	
					# Set the height to -1 if the cell is visited
                    heightMap[i][j] = -1

        return res
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print(trapRainWater2(heightMap))
