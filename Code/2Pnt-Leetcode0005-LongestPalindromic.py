def longestPalindrome(s: str) -> str:
        longest = ''
        def findLongest(s, l, r):
            while l>=0 and r<len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        for i in range(len(s)):
            s1 = findLongest(s, i, i)
            print('s1', s1, i)
            if len(s1) > len(longest): longest = s1
            
            s2 = findLongest(s, i, i+1)
            print('s2', s2)
            if len(s2) > len(longest): longest = s2
        print(longest)                
        return longest

longestPalindrome('bababa')
