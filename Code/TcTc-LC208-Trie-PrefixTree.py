import collections
class Node(object):
    def __init__(self):
        self.children = collections.defaultdict(Node)
        self.isword = False
        
class Trie(object):
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for w in word:
            print('\t', w)
            current = current.children[w]
        print(word)
        current.isword = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        i = 0
        for w in word:
            i += 1
            current = current.children.get(w)
            if current == None:
                print('i=', i)
                return False
        print('i=', i)
        return current.isword

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for w in prefix:
            current = current.children.get(w)
            if current == None:
                return False
        return True        


obj = Trie()
for word in ['A', 'to', 'tea', 'ted', 'ten', 'i', 'in',  'inn']:
    obj.insert(word)
print('tea', obj.search('tea'))
print('te', obj.search('te'))
#param_3 = obj.startsWith(prefix)
