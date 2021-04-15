def canPlaceFlowers(flowerbed, n):
        res = 0
        flowerbed = [0] + flowerbed + [0] ## clever way to handle edge cases
        print('\t',flowerbed)
        for i in range(1, len(flowerbed)-1):
            #l = 0 if i == 0 else flowerbed[i-1]
            #r = 0 if i == n-1 else flowerbed[i+1]
            #if l == 0 and r == 0 and flowerbed[i] == 0:
            if 0 == flowerbed[i-1] and 0 == flowerbed[i+1] and flowerbed[i] == 0:
                flowerbed[i] = 1
                res += 1
            print(i, res, flowerbed)

        #return res == n
        return res >= n;
print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1,0,0], 2))
