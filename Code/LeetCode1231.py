def solve(sweetness, K):
    print(sweetness, K)
    Sum = sum(sweetness)
    n  = len(sweetness)
    K += 1
    def check(m):
        cnt = 0
        cur_sum = 0
        for i in range(n):
            cur_sum += sweetness[i]
            print('\tcur_sum=', cur_sum, m, K)
            if cur_sum >= m:
                cur_sum = 0
                cnt += 1
                print('\t\tcnt=', cnt, K)
                if cnt >= K:
                    print('\t\t\tcnt=', cnt, K)
                    return True
        return False

    l, r = 0, Sum
    while l<r:
        m = l + (r-l)//2
        print(l,r,m)
        if check(m+1): l = m+1
        else: r = m
    return l


sweetness = [1,2,3,4,5,6,7,8,9];
K = 5
print(solve(sweetness, K))
