from typing import List

def storage_optimization(n: int, m: int, h: List[int], v: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    max_h = 1
    i = 1
    while i <= n:
        temp = 1
        while i in h:
            i += 1
            temp += 1
        else:
            i += 1
        max_h = max(max_h, temp)
        
    max_v = 1
    i = 1        
    while i <= m:
        temp = 1
        while i in v:
            i += 1
            temp += 1
        else:
            i += 1
        max_v = max(max_v, temp)        
            
    return max_h*max_v

if __name__ == '__main__':
    n = int(input())
    m = int(input())
    h = [int(x) for x in input().split()]
    v = [int(x) for x in input().split()]
    res = storage_optimization(n, m, h, v)
    print(res)
