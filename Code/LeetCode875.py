from math import ceil
def minEatingSpeed(piles, h) :
        def canfinish(K):
            hours_needed = 0
            for p in piles:
                hours_needed+= ceil(p/K) #doing the cummulative sum
            return hours_needed <= h   
    # here we are taking k b/w the range of 1, max(piles)
        l = 1
        r = max(piles)

        while l<r:
            m = (l+r)//2
            print(l,m,r)
            if canfinish(m):# we are checking if we can finish with mid speed
                r = m      #if yes then we will see if there is anything min than this 
                              # and the reason we are not making the r = mid -1 coz 
                              # then if our mid would be the required k then we might miss it.
            else:
                l = m+1

        return r
piles = [3,6,7,11]; h = 8
print(minEatingSpeed(piles, h))
