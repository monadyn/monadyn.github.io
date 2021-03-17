import collections
def ladderLength(beginWord, endWord, wordList):
        wordset = set(wordList)
        queue = collections.deque()
        queue.append((beginWord, 1))
        word_length = len(beginWord)
        while queue:
            word, step = queue.popleft()
            if word == endWord:
                return step

            #We traversal all elements of the tree once so total time complexity is O(n)
            for i in range(word_length):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i]+c+word[i+1:]
                    if newWord in wordset:
                        wordset.remove(newWord)
                        queue.append((newWord, step+1))
        return 0
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
wordList = ["hot","dot","dog","lot","log","cog"]

print(ladderLength(beginWord, endWord, wordList))
