from task5_BST import *
import timeit
class HashTable:

    def __init__(self, table_capacity=11, hash_base=31):

        """
        Creates a new hash table, with initial table capacity 'table_capacity', \
        and with using base,  'hash_base' for the hash function (see hash below). \
        If table_capacity or hash_base are not specified, the hash table should use appropriate default values
        table_capacity = 11, hash_base = 31.



        @:param self: the object
        @:param table_capacity: The initial size of the hash table array.
        @:param hash_base: The value of the base used in the hash function.
        @:return: Return None

        @pre-condition: table_capacity and hash_base both have to be positive integers.
        @post-condition: The hash table is initialised with each element set to 'None'
        @complexity: Worst-Case: O(1)
        @complexity: Best-Case: O(1)

        """

        self.table_capacity = table_capacity
        self.hash_base = hash_base
        self.array = [None] * self.table_capacity  # Array initialized with 'None" in each element.
        self.count = 0  # the number of items in the table, initially set to '0'



    def __getitem__(self, key):
        """
        This Function Returns the value corresponding to key in the hash table.
        Raises a KeyError if key does not exist in the hash table.
        Remember that this can be called from Python code as table[key]

        @:param self: the object
        @:param key: key of the element being seeked in the hash table

        @pre-condition: Key must exist in hash table.
        @post-condition:  Return value corresponding to the key.
        @complexity: Worst-Case: log(n),  (n is the capacity of the hash table)
        @complexity: Best-Case: O(1) - if key is the root

        """
        position = self.hash(key)

        try:
            if self.array[position] is None:
                raise KeyError("Key does not exist)")
            bst = self.array[position]
            return bst[key]
        except KeyError as error:
            print(error)



    def __setitem__(self, key, value):

        """
        Sets the value corresponding to key in the hash table to be value.
        Called as table[key] = value

        @:param self: the object
        :param key: Unique key corresponding to the Data in Value, serves as a unique identifier for the value
        :param value: the data to be entered alongside the key in the tuple, occupying the second indexed position in the tuple
        :return: None
        @pre-condition: Key must be valid.
        @post-condition: The Key - Value pair inserted into the hash table.
        @complexity: Worst-Case: log(n), (n being the capacity of the hash table)
        @complexity: Best-Case: O(1) - if key is the root

        """
        position = self.hash(key)
        if self.array[position] is not None:
            self.array[position].__setitem__(key, value)
        else:
            my_tree = BinarySearchTree()
            my_tree.__setitem__(key, value)
            self.array[position] = my_tree

    def hash(self, key):
        """
        function calculates a hash value, given the parameter key

        :param key: The key for which hash calculated
        :return: Hash value of key.
        @pre-condition: key must be valid
        @post-condition: Calculate Hash value for key
        @complexity: Worst-Case: O(1)
        @complexity: Best-Case: O(1)

        """
        key = str(key)
        h = 0
        a = self.hash_base
        for i in range(len(str(key))):
            h = (h * a + ord(key[i])) % self.table_capacity
        return h

    def __contains__(self, key):
        """
        Returns True if key is in the table and False otherwise.

        :param key: Unique key corresponding to the Value (in the Key- Value Pair), serves as a unique identifier for the value
        :return: True / False
        @pre-condition: key must be valid
        @post-condition: locate key in hash table. Returns True if found, or returns false otherwise.
        @complexity: Worst-Case: log(n)
        @complexity: Best-Case: O(1) - if key is the root

        """
        position = self.hash(key)

        if self.array[position] is None:
            return False
        try:
            self.__getitem__(key)
            return True
        except KeyError:
            return False

# ______________________________________________________________________________________________________________________

#Testing
# y=HashTable(11,31)
# for i in range (50):
#     h=y.hash(i)
#     if (h == 0):
#         print(i)
# 7
# 16
# 28
# 41

# y = HashTable(11,31)
# y[7] = 7
# y[16]= 16
# y[28] = 28
# y[41] = 41
#
# print(y.array[0].root.children[1].children[1].children[1])



# ______________________________________________________________________________________________________________________




def load_dictionary(hash_table, filename):

    file = open(filename)
    lines = file.readlines()
    start = timeit.default_timer()
    for line in lines:
        hash_table.__setitem__(line.rstrip(),1)
        if timeit.default_timer() - start > 10:
            break
    file.close()

# h_table = HashTable()
# load_dictionary(h_table,'english_small.txt')
# print(h_table.count)


def dictionary_function():

    hash_base_values = [1, 27183, 250726]
    table_size_values = [250727, 402221, 1000081]
    filename = ["english_small.txt", "english_large.txt","french.txt"]

    for file in filename:
        filename = file
        print("\n\n" + str(filename) + "\n")

        b_str = "b"
        table_size_str = "TABLESIZE"
        time_str = "Time (s)"
        print ("%-15s %-15s %-15s" % (b_str, table_size_str, time_str))

        for hash_base in hash_base_values:
            for table_size in table_size_values:
                hash_table = HashTable(table_size, hash_base)
                start = timeit.default_timer()
                load_dictionary(hash_table, file)
                time = timeit.default_timer() - start
                time = round(time, 6)
                if time > 10:
                    time = "TIMEOUT"
                print("%-15s %-15s %-15s " % (str(hash_base) ,str(table_size),str(time) ))



# ______________________________________________________________________________________________________________________


if __name__ == '__main__':
    dictionary_function()

# ______________________________________________________________________________________________________________________


"""

TimeOut Time = 10 Seconds 


english_small.txt

b               TABLESIZE       Time (s)       
1               250727          9.040908        
1               402221          8.764729        
1               1000081         8.636529        
27183           250727          0.611154        
27183           402221          0.538894        
27183           1000081         0.564934        
250726          250727          TIMEOUT         
250726          402221          0.592082        
250726          1000081         0.55851         


english_large.txt

b               TABLESIZE       Time (s)       
1               250727          TIMEOUT         
1               402221          TIMEOUT         
1               1000081         TIMEOUT         
27183           250727          1.491416        
27183           402221          1.397844        
27183           1000081         1.457372        
250726          250727          TIMEOUT         
250726          402221          1.611134        
250726          1000081         1.538529        


french.txt

b               TABLESIZE       Time (s)       
1               250727          TIMEOUT         
1               402221          TIMEOUT         
1               1000081         TIMEOUT         
27183           250727          1.696485        
27183           402221          1.952941        
27183           1000081         1.698681        
250726          250727          TIMEOUT         
250726          402221          1.601872        
250726          1000081         1.650281        

Process finished with exit code 0


Explaination:

There are 9  HashBase (b) and TableSize combinations. 
We record the varying ammount of tme taken to insert words into the HashTable of each of the 9 combinations of 
HashBase and TableSize. 
The combinations of TableSize and HAshBAse that take longer than 10 seconds to complete are recorde with a TimeOut message

When the HashBase is small (eg. 1) , and TableSize is increasingly larger, it takes increasingly larger ammount of time for 
all the words to be inserted into the HashTable, thus resulting in a TimeOut (when time increases more than present Timeout period)
This longer ammount of time is because there are many collisions and hence BST's are is used to solve these collisions. 
When the Keys of multiple elements hash to the same value, all the elements of the same key are added to the Binary Search Tree 
created at that poaition in the hash table. the multiple elements with same keys are added as 'children' of the root.
Also,since the HashBase is small the possibilities for unique hash values is limited.
Therefore the probability of keys many elements hashing to the same value, is extremely high, resulting in more collisions. 
This is made evident for when  HashBase is 1 and TableSize is increasingly larger, the execution always TimesOut.
This is because multiple elements have keys that hash to the same value resulting in the creation of BST's in that 
position, and as more keys hash to the same value, the BST's increasingly grow in depth (more children). 
Thus leading to a increase in execution time leading to a Timeut.
Therefore having larger HashBase makes it more feasible to create unique hash values, for the positions of tuples.
Thereby making the elements with keys hashing to the same hash value, fewver and far in between. Thus making the BST's 
more spread out and more shallow in depth (fewer children). 


The number of collisions is also impacted by the TableSize. Because for the universal HashFunction the number of collisions 
is inversely proportional to TableSize, collisions = 1/TableSize. Therefore to minimize collision the TableSize should 
be large and a prime number. When TableSize is Large and Prime, fewer collisions take place therefore smaller execution time. 
This is made evident when HashBase is 27183 and TableSize is increasingly larger, and as TableSize increases the execution time drops 
since there are fewer collisions. This is further highlighted by the Decreasing number of Collision Count since collisions is 
inversely proportional to Tablesize, as the table size increases with constant HashBase (27183). 
Therefore fewver collisions, means fewer keys hash to the same value, therefore the BST's created in those positions are 
more shallow in depth (fewver children) and therefore smaller execution time. This is why the Seperate Chaining takes 
less time compared to both Linear Probing and Quadratic Probing. 

When HashBase = 250726 and TableSize = 250727, this times out since the HashBase and TableSize are very close and 
hashbase is not a prime.
Also when hashBase = 250726 (largest) and Tablesize is consecutivley larger, the execution time is not significantly less 
, meaning collision count, is not much less than for other values of HashBase.
very much less compared to other times for same TableSize this is because the HashBase is not prime. 
Therefore there are slightly fewer number of collisions, therefore slighly more shallow (fewer children) BST's 
at the positions of collisions, resulting in a slightly smaller execution time.  



When compared to Linear Probing and Quadratic Probinf the execution time, is  smaller on all accounts of HashBase 
and TableSize. 
This is because there is much less time consumed on probing. If many keys hash to the same value, a BST is created at 
that position and all the keys with same hash is added to the BST as children of the root (first key to hash to that position).


"""