def f(lst, l):
    res = 0
    for i in lst:
        if isinstance(i, list):
            res += f(i,l+1)
        else:
            res += i*l
    return res
lst = [1,[4,[6]]]
lst = [[1,1],2,[1,1]]
l = 1
print(f(lst, l))
