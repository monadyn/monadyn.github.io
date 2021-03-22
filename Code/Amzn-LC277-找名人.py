def findCelebrity(n):
        """
        :type n: int
        :rtype: int
        First traverse n people to find possible candidates cand, according to the definition of celebrities, celebrities are everyone knows him, but he does not know others. 
        So, when knowns(cand, i) is true, cand needs to be updated to i 
        According to the meaning of the question, there is at most one celebrity among n people, then the cand after the traversal is the candidate. 
        
        Then traverse n people, according to the definition to determine whether the cand is a celebrity.
Time: O(2*n)
Space: O(1)
        """
        cand = 0
        for i in range(1, n):
            if knows(cand, i):
                cand = i
                
        for i in range(n):
            if i != cand and (not knows(i, cand) or knows(cand, i)):
                return -1
        return cand
