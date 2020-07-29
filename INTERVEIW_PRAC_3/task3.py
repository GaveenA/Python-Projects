import timeit
class HashTable:

    def __init__(self, table_capacity=101, hash_base=31):

        """
        Creates a new hash table, with initial table capacity 'table_capacity', \
        and with using base,  'hash_base' for the hash function (see hash below). \
        If table_capacity or hash_base are not specified, the hash table should use appropriate default values
        table_capacity = 10, hash_base = 31.



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
        self.rehash_count = 0
        self.probe_array = []



    def __getitem__(self, key):
        """
        This Function Returns the value corresponding to key in the hash table.
        Raises a KeyError if key does not exist in the hash table.
        Remember that this can be called from Python code as table[key]

        @:param self: the object
        @:param key: key of the element being seeked in the hash table

        @pre-condition: Key must exist in hash table.
        @post-condition:  Return value corresponding to the key.
        @complexity: Worst-Case: O(n),  (n is the capacity of the hash table)
        @complexity: Best-Case: O(1)

        """
        position = self.hash(key)

        for _ in range(self.table_capacity):
            if self.array[position] is None:
                raise KeyError(key)
            elif self.array[position][0] == key:
                return self.array[position][1]
            else:
                position = (position + 1) % self.table_capacity
        raise KeyError(key)


    def is_full(self):
        """
        This method informs the user if hash table is full.
        Returns True if if the hash table is full and False otherwise.

        @:param self: the object.
        @:param table_capacity: The initial size of the hash table array.
        @:param hash_base: The value of the base used in the hash function.
        @:return: Return None


        @pre-condition: None
        @post-condition: None
        @complexity: Worst-Case: O(1)
        @complexity: Best-Case: O(1)

        """

        return self.count == len(self.array)



    def insert(self, key, value):
        """
        Insert given key and data as a tuple into hashtable.

        @:param self: the object
        :param key: Unique key corresponding to the Data in Value, serves as a unique identifier for the value
        :param value: the data to be entered alongside the key in the tuple, occupying the second indexed position in the tuple
        :return: None
        @pre-condition: Key must be valid.
        @post-condition: The Key - Value pair inserted into the hash table.
        @complexity: Worst-Case: O(n), (n being the capacity of the hash table)
        @complexity: Best-Case: O(1)

        """
        # If the array is full, call rehash function

        key = str(key)
        position = self.hash(key)
        probe_count = 0
        insert_done = False

        for _ in range(self.table_capacity):
            if self.array[position] is None:
                self.array[position] = (key, value)  # if the element at the position is 'None', insert tuple directly.
                self.count += 1
                insert_done = True
                break
            elif self.array[position][0] == key:
                # if the key in the tuple at the position corresponds to the given key; the element is already present\
                # and only the data of the tuple needs to be updated,
                # in order to do this a new tuple is created as tuples are immutable.
                self.array[position] = (key, value)
                insert_done = True
                break
            else:    # Checking next Position
                position = (position + 1) % self.table_capacity
                probe_count += 1

        if probe_count > 0 and insert_done:
            self.probe_array.append(probe_count)

        if self.is_full() and not insert_done:
            self.rehash()
            self.insert(key, value )

    def __setitem__(self, key, value):

        """
        Sets the value corresponding to key in the hash table to be value.
        If the hash table is full and the key does not exist in the table yet,
        it first calls the rehash method (see below) and then reinserts the key and value.
        Called as table[key] = value

        @:param self: the object
        :param key: Unique key corresponding to the Data in Value, serves as a unique identifier for the value
        :param value: the data to be entered alongside the key in the tuple, occupying the second indexed position in the tuple
        :return: None
        @pre-condition: Key must be valid.
        @post-condition: The Key - Value pair inserted into the hash table.
        @complexity: Worst-Case: O(n), (n being the capacity of the hash table)
        @complexity: Best-Case: O(1)

        """
        self.insert(key, value)

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

        :param key: Unique key corresponding to the Data in Value, serves as a unique identifier for the value
        :return: True / False
        @pre-condition: key must be valid
        @post-condition: locate key in hash table. Returns True if found, or returns false otherwise.
        @complexity: Worst-Case: O(n)
        @complexity: Best-Case: O(1)

        """
        position = self.hash(key)

        for _ in range(self.table_capacity):
            if self.array[position] is None:
                return False
            elif self.array[position][0] == key:
                return True
            else:
                position = (position + 1) % self.table_capacity
        return False


    def rehash(self):
        """
        It first creates a new array using as size the smallest prime number in
        the Primes list below that is larger than twice the current size.
        It then updates the size of the hash table and reinserts all key-value pairs in the old array into
        the new array using the new size. Raises a ValueError if there is no such prime in the list.
        For now, this method is only called when the table is full and we want to insert an element.

        @:param self: the object
        :return: None

        @pre-condition: The hashtable must be full for rehash to be run.
        @post-condition: Table capacity is increased, with the original elements re-inserted using new hash values.
        @complexity: Worst-Case: O(m*n),  (m is initial table_capacity and n is the table_capacity after increasing)
        @complexity: Best-Case: O(1)

        """
        primes = [3, 7, 11, 17, 23, 29, 37, 47, 59, 71, 89, 107, 131, 163, 197, 239, 293, 353, 431, 521, 631, 761,
                  919, 1103, 1327, 1597, 1931, 2333, 2801, 3371, 4049, 4861, 5839, 7013, 8419, 10103, 12143, 14591,
                  17519, 21023, 25229, 30293, 36353, 43627, 52361, 62851, 75431, 90523, 108631, 130363, 156437,
                  187751, 225307, 270371, 324449, 389357, 467237, 560689, 672827, 807403, 968897, 1162687, 1395263,
                  1674319, 2009191, 2411033, 2893249, 3471899, 4166287, 4999559, 5999471, 7199369]

        temp_list = []
        for i in self.array:
            if i is not None:
                temp_list.append(i)

        self.table_capacity = 2 * self.table_capacity


        try:
            for i in range(len(primes)):
                if primes[i] > self.table_capacity:
                    self.table_capacity = primes[i]
                    break
                elif i == (len(primes) -1) :
                    if not primes[i] > self.table_capacity:
                        raise ValueError("There is no prime in the list such that prime > " + self.table_capacity)
        except Exception as error:
            print(error)

        self.array = [None] * self.table_capacity
        self.count = 0
        for element in temp_list:
            self.insert(element[0], element[1])

        self.rehash_count += 1



    def statistics(self):
        """
        which returns a tuple (collision count, probe total, probe max, rehash count), consisting of:
        (a) the total number of collisions,
        (b) the total length of the probe chains,
        (c) the length of the longest probe chain, and
        (d) the number of times rehash has been called.

        :return: (collision count, probe total, probe max, rehash count)

        """
        # collision_count = len(self.probe_count_array)
        # probe_total = sum(self.probe_count_array)
        # probe_max = max(self.probe_count_array)

        collision_count = len(self.probe_array)
        probe_total = sum(self.probe_array)
        rehash_count = self.rehash_count
        if len(self.probe_array) == 0:
            probe_max = 0
        else:
            probe_max = max(self.probe_array)

        return (collision_count, probe_total, probe_max, rehash_count)


#_______________________________________________________________________________________________________________________



#Testing
# hash_table = HashTable(7, 31)
# # lecture_keys = ['Aho', 'Standish', 'Langsam', 'Sedgewick', 'Knuth', 'Kruse', 'Horowiz']
# # for element in lecture_keys:
# #     hash_table.insert(element, 1)
# # print(hash_table.array)
# # hash_table.insert('abo',1)
# # hash_table.insert('oha',1)
# # print(hash_table.array)
# # print(hash_table.table_capacity)
# # print(hash_table.statistics())

# x = HashTable(6,31)
# for i in range(50):
#     if x.hash(i) == 0:
#         print(i)
#
# for i in [2,7,13,18,22,27]:
#     x.insert(i,i)
#     print(x.array)
# x[22] = "gaveen"
# print(x.array)




#_______________________________________________________________________________________________________________________


def load_dictionary(hash_table, filename):
    """
    This function serves to
    :param hash_table:
    :param filename:
    :return:
    """

    file = open(filename)
    lines = file.readlines()
    start = timeit.default_timer()
    for line in lines:
        hash_table.insert(line.rstrip(),1)
        if timeit.default_timer() - start > 4:
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
        collision_count_str = "Collision Count"
        probe_total_str = "Probe Total"
        probe_max_str = "Probe Max"
        rehash_count = "Rehash Count"



        print ("%-15s %-15s %-15s %-20s %-15s %-15s %-15s" % (b_str, table_size_str, time_str, collision_count_str, probe_total_str, probe_max_str, rehash_count))

        for hash_base in hash_base_values:
            for table_size in table_size_values:
                hash_table = HashTable(table_size, hash_base)

                start = timeit.default_timer()
                load_dictionary(hash_table, file)
                time = timeit.default_timer() - start
                time = round(time, 6)

                stats = hash_table.statistics()

                collision_count = stats[0]
                probe_total = stats[1]
                probe_max = stats[2]
                rehash_count = stats[3]

                if timeit.default_timer() - start > 4:
                    time = "TIMEOUT"
                print("%-15s %-15s %-15s %-20s %-15s %-15s %-15s" % (str(hash_base) ,str(table_size),str(time) , str(collision_count), str(probe_total), str(probe_max), str(rehash_count) ))




# ______________________________________________________________________________________________________________________



if __name__ == '__main__':
    dictionary_function()


# ______________________________________________________________________________________________________________________




"""

english_small.txt

b               TABLESIZE       Time (s)        Collision Count      Probe Total     Probe Max       Rehash Count   
1               250727          TIMEOUT         5368                 12988909        5628            0              
1               402221          TIMEOUT         5454                 13442215        5678            0              
1               1000081         TIMEOUT         5466                 13505795        5678            0              
27183           250727          0.416619        14265                22543           21              0              
27183           402221          0.409192        9000                 11736           13              0              
27183           1000081         0.394524        3489                 3910            5               0              
250726          250727          TIMEOUT         5152                 13168563        5186            0              
250726          402221          0.413448        9010                 11798           10              0              
250726          1000081         0.381206        3606                 4047            8               0              


english_large.txt

b               TABLESIZE       Time (s)        Collision Count      Probe Total     Probe Max       Rehash Count   
1               250727          TIMEOUT         5450                 13257994        5693            0              
1               402221          TIMEOUT         5508                 13561500        5693            0              
1               1000081         TIMEOUT         5474                 13383785        5693            0              
27183           250727          1.128808        76624                420489          278             0              
27183           402221          0.945948        47798                100107          43              0              
27183           1000081         0.951693        19038                24410           15              0              
250726          250727          TIMEOUT         5150                 13151246        5196            0              
250726          402221          0.982607        47903                101113          51              0              
250726          1000081         0.931135        19047                24487           13              0              


french.txt

b               TABLESIZE       Time (s)        Collision Count      Probe Total     Probe Max       Rehash Count   
1               250727          TIMEOUT         5408                 12988986        5566            0              
1               402221          TIMEOUT         5455                 13231556        5566            0              
1               1000081         TIMEOUT         5538                 13652312        5566            0              
27183           250727          1.29894         85022                565691          299             0              
27183           402221          1.076091        53377                124796          57              0              
27183           1000081         1.055777        22045                30701           21              0              
250726          250727          TIMEOUT         5421                 13185493        5487            0              
250726          402221          1.105635        53157                122372          49              0              
250726          1000081         1.11451         21708                29927           12              0              

Process finished with exit code 0


Explaination:

There are 9  HashBase (b) and TableSize combinations. 
We record the varying ammount of tme taken to insert words into the HashTable of each of the 9 combinations of 
HashBase and TableSize. 
The combinations of TableSize and HAshBAse that take longer than 10 seconds to complete are recorde with a TimeOut message

When the HashBase is small (eg. 1) , and TableSize is increasingly larger, it takes increasingly larger ammount of time for 
all the words to be inserted into the HashTable, thus resulting in a TimeOut (when time increases more than present Timeout period)
This longer ammount of time is because there are many collisions and hence linear probing is used to solve these collisions. 
This is made evident by the significantly larger Probe Totals and Probe Max values, meaning that to resolve the similar Number
of collisions,  more probes(greater probe total) and larger Probe Max (longer probe chain) must be done as the hashbase is very small. 
Therefore longer probe chains and greater probe totals result in longer execution time.
Also,since the HashBase is small the possibilities for unique hash values is limited. 
Therefore the probability of keys many elements hashing to the same value, is extremely high, resulting in more collisions.   
This is made evident for when  HashBase is 1 and TableSize is increasingly larger, the execution always TimesOut.
Therefore having larger HashBase makes it more feasible to create unique hash values, for thr positions of tuples.


The number of collisions is also impacted by the TableSize. Because for the universal HashFunction the number of collisions 
is inversely proportional to TableSize, collisions = 1/TableSize. Therefore to minimize collision the TableSize should 
be large and a prime number. When TableSize is Large and Prime, fewer collisions take place therefore smaller execution time. 
This is made evident when HashBase is 27183 and TableSize is increasingly larger, and as TableSize increases the execution time drops 
since there are fewer collisions. This is further highlighted by the Decreasing number of Collision Count since collisions is 
imversely proportional to Tablesize, smaller Probe Totals and smaller probe chains (smaller probe Max), 
as the table size increases with constant HashBase (27183)

When HashBase = 250726 and TableSize = 250727, this times out since the HashBase and TableSize are very close and hashbase is not a prime.
Also when hashBase = 250726 (largest) and Tablesize is consecutivley larger, the execution time is not significantly less 
and collision count, probe total, probe max is not much less than for other values of HashBase
this is because the HashBase is not prime. 
    
"""