i = 0
def depthSumInverse(nestedList):
        def dfs(nestedList, list_sum, i):
            print('>'*i,nestedList, list_sum)
            temp_list = []
            for elem in nestedList:
                if not isinstance(elem, list):
                    list_sum += elem
                else:
                    temp_list += elem
            if len(temp_list) != 0:
                list_sum+=dfs(temp_list, list_sum, i+1)
            print('<'*i,nestedList, list_sum)
            return list_sum
        return dfs(nestedList, 0, 1)
lst = [1,[4,[6]]]
lst = [[1,1],2,[1,1]]
lst = [1,[4,[6]]]
print(depthSumInverse(lst))
