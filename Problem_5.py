import hashlib
from datetime import datetime
from pytz import timezone


class Blockchain:
    def __init__(self):
        self.previous_hash = 0
        self.tail = None
    
    def append(self, transaction_data = None):
        assert transaction_data is not None
        
        newblock = Block(transaction_data)
        newblock.previous_block = self.tail
        self.tail = newblock
        self.tail.previous_hash = self.previous_hash
        self.previous_hash = self.tail.calc_hash()

                                
class Block:

    def __init__(self, transaction_data):
        self.timestamp = datetime.now(timezone('GMT'))
        self.transaction_data = transaction_data
        self.previous_hash = None
        self.previous_block = None
        
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.timestamp).encode('utf-8') + str(self.transaction_data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()
      
      
chain = Blockchain()

try:
    chain.append(4)
    print("current block data =", chain.tail.transaction_data, "\ncurrent block timestamp =", chain.tail.timestamp, "\nprevious hash =",chain.tail.previous_hash, "\n")
except TypeError:
    print("You have entered too many values\n")
except AssertionError:
    print("There is no value to append\n")
    
try:
    chain.append("Hello!")
    print("current block data =", chain.tail.transaction_data, "\ncurrent block timestamp =", chain.tail.timestamp, "\nprevious hash =",chain.tail.previous_hash, "\n")
except TypeError:
    print("You have entered too many values\n")
except AssertionError:
    print("There is no value to append\n")
    
try:
    chain.append()
    print("current block data =", chain.tail.transaction_data, "\ncurrent block timestamp =", chain.tail.timestamp, "\nprevious hash =",chain.tail.previous_hash, "\n")
except TypeError:
    print("You have entered too many values\n")
except AssertionError:
    print("There is no value to append\n")
#no value to append

try:
    chain.append("a","b")
    print("current block data =", chain.tail.transaction_data, "\ncurrent block timestamp =", chain.tail.timestamp, "\nprevious hash =",chain.tail.previous_hash, "\n")
except TypeError:
    print("You have entered too many values\n")
except AssertionError:
    print("There is no value to append\n")
#too many values

