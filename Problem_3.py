import sys

class Node:
    def __init__(self, name = None):
        self.name = name
        self.child_0 = None
        self.child_1 = None
        self.visited = False

def huffman_encoding(data):
    mydict = dict()
    encoded = ""
    
    assert type(data) is str
    
    for char in data:
        mydict[char] = mydict.get(char, 0) + 1
     
    while len(mydict) >= 2:
        build (mydict)
    
    root = list(mydict.keys())[0]
    chiffre_dict = (chiffre(root, root, ""))
    
    for i in data:
        encoded += chiffre_dict.get(i)

    return encoded, root    


def build(mydict):
    key0 = (min(mydict, key = mydict.get))
    freq0 = mydict.pop(key0)
    
    if type(key0) is str:
        node0 = Node(key0)
    else:
        node0 = key0

    key1 = (min(mydict, key = mydict.get))
    freq1 = mydict.pop(key1)
    
    if type(key1) is str:
        node1 = Node(key1)
    else:
        node1 = key1

    bignode = Node()
    bignode.child_1 = node1
    bignode.child_0 = node0
    mydict.update({bignode:freq1 + freq0})
     
     
def chiffre(curr, root, code):
    translator:dict = dict()
    
    if curr.child_0 is None and curr.child_1 is None:
        curr.visited = True
        translator = ({curr.name : code})
        
    else: 
        if curr.child_0.visited == False:
            translator.update(chiffre(curr.child_0, root, code + "0"))
            
        if curr.child_1.visited == False:
            translator.update(chiffre(curr.child_1, root, code + "1"))
        
    return translator


def huffman_decoding(data,tree):
    decoded = ""
    root = tree
    i = 0
    while i < len(data):
        digit = data[i]
        if digit == "0" and tree.child_0 is not None:
            tree = tree.child_0
            i += 1
        elif digit == "1" and tree.child_1 is not None:
            tree = tree.child_1
            i += 1
        else:
            decoded += tree.name
            tree = root
    decoded += tree.name
    return decoded


if __name__ == "__main__":
    
    try:
        a_great_sentence = "The bird is the word"
        
        encoded_data, tree = huffman_encoding(a_great_sentence)

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))


        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))
        
        print("Does the decoded string match the original string?", a_great_sentence == decoded_data, "\n")
    except IndexError:
        print("The string to be encoded cannot be empty\n")
    except AssertionError:
        print("The data to be encoded must be a string\n")
#the decoded data matches the input and its size is smaller

    
    
    try:
        a_great_sentence = ""
        
        encoded_data, tree = huffman_encoding(a_great_sentence)
        
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))
        
        print("Does the decoded string match the original string?", a_great_sentence == decoded_data, "\n")
    except IndexError:
        print("The string to be encoded cannot be empty\n")
    except AssertionError:
        print("The data to be encoded must be a string\n")
#index error - string cannot be empty
    
    
    try:
        a_great_sentence = 765

        encoded_data, tree = huffman_encoding(a_great_sentence)
        
        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))
        
        print("Does the decoded string match the original string?", a_great_sentence == decoded_data, "\n")
    except IndexError:
        print("The string to be encoded cannot be empty\n")
    except AssertionError:
        print("The data to be encoded must be a string\n")
#assertion error - the input is a string type        

