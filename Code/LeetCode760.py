from pprint import pprint
import collections

class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        # build a dict d[val] = [index]
        d = collections.defaultdict(list)
        dd = {}
        for i, val in enumerate(B):
            d[val].append(i)
            dd[val] = i
        pprint(d)
        pprint(dd)
        #return [d[val].pop() for val in A]
        return [dd[val] for val in A]



s = Solution()
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]

print(s.anagramMappings(A, B))
