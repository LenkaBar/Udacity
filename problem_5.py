class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def insert(self, char):
        self.children.update({char : TrieNode()})
        
    def suffixes(self, suffix = ''):
        
        output = self.recursion(suffix, list())
        if output == [""]:
            return "Your input is a word but it doesn't form other words"
        return output
        
    def recursion(self, suffix, output):

        for key in self.children.keys():      
            output = self.children[key].recursion(suffix + key, output) #enter recursion for all children
        
        if self.is_word == True:
            output.append(suffix)
            
        return output
        

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        
        for char in word:
            if char not in current.children:
                current.insert(char)
                
            current = current.children[char]
            
        current.is_word = True
        

    def find(self, prefix):
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return -1
            current = current.children[char]
            
        return current
        ## Find the Trie node that represents this prefix


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    
    
#code for testing in jupyter
"""
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');
"""

try:
    node1 = MyTrie.find("an")
    print(node1.suffixes())
except AttributeError:
    print("The string you have specified forms no words")
#['thology', 'tagonist', 'tonym', 't']

try:
    node2 = MyTrie.find("")
    print(node2.suffixes())
except AttributeError:
    print("The string you have specified forms no words")
#should print the entire contents of the Trie

try:
    node3 = MyTrie.find("xyz")
    print(node3.suffixes())
except AttributeError:
    print("The string you have specified forms no words")
#forms no words
    
try:
    node4 = MyTrie.find("antagonist")
    print(node4.suffixes())
except AttributeError:
    print("The string you have specified forms no words")
#is a word but doesn't form other words