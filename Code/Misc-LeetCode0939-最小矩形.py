import sys
def minAreaRect(points):
        #TC: O(N^2)
        #SC: O(N^2)
        #N number of total points, N = len(N)
        #Each rectangle is determined by 2 points.
        #Through loop through every two points and use these two points to determine coordinates of other two points

        n = len(points)
        res = sys.maxsize

        Set = set()
        for x,y in points:
            Set.add((x,y))                 

        for x1,y1 in points:
            for x2,y2 in points:
                if x1 > x2 and y1 > y2:
                    if (x1,y2) in Set and (x2,y1) in Set:
                        area = abs(y1-y2) * abs(x1-x2)
                        res = min(res, area)

        if res == sys.maxsize:
            return 0
        else:
            return res
points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
print(minAreaRect(points))
