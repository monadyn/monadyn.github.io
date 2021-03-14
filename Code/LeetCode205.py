def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        print(set(zip(s, t)))
        print(set(s))
        print(set(t))
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

print(isIsomorphic('paper', 'title'))
