class Solution:
    def partition(self, s):
        def backtrack(s, res, path):
            print('\ts=',s,'path=', path)
            if not s: res.append(path)
            else:
                for i in range(1, len(s) + 1):
                    print('\t\t',s[: i] )
                    if isPalindrome(s[: i]):
                        backtrack(s[i: ], res, path + [s[: i]])
        
        isPalindrome = lambda x: x == x[:: -1]
        res = []
        backtrack(s, res, [])
        return res
s = Solution()
#print(s.partition("aabcb"))
print(s.partition("efe"))
