from collections import defaultdict
def findRedundantConnection(edges):
        parent = defaultdict(int) 
        def find(v): #findind  representavive 
            if parent[v] == 0:
                print('\t\tfind', parent, v)
                return v 
            print('\t\tfind', v, parent[v])
            return find(parent[v])

        def union(u, v): #merging u and v's representavtive 
            if 0: parent[find(u)] = find(v) 
            else:
                x_set = find(u)
                y_set = find(v) 
                print('\t\tunon', u, x_set)
                print('\t\tunon', v, y_set)
                parent[x_set] = y_set 
                print('\t\tunon', parent)
        answer = []
        for u, v in edges: #no need to form a graph😁
            print('check:' , u, v)
            x = find(u) 
            print('\tafter finding representavive, u=',u, x, parent)
            y = find(v) 
            print('\tafter finding representavive, v=',v, y, parent)
            
            if x == y and u < v:
                    answer = [u, v] 
            else:
                    union(x, y) 
            print('\t',parent)
        return answer 


g = [[1,2], [2,3], [3,4], [1,4], [1,5]]
print(findRedundantConnection(g))
