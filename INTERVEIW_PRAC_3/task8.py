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
        insert_done = False

        # probe up to array size
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
            else:  # Checking next Position
                position = (position + 1) % self.table_capacity
        if self.is_full() and not insert_done:
            self.rehash()
            self.insert(key, value)


    def __setitem__(self, key, value):

        """
        Sets the value corresponding to key in the hash table to be value.
        If the hash table is full and the key does not exist in the table yet,
        it first calls the rehash method (see below) and then reinserts the key and value.
        Called as table[key] = value

        :param self: the object
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







    def delete(self, key):

        """

        This function is to take key as input and then delete the entry corresponding to that key,
        reinserting all elements from the position where the key appears, until the first empty position.
        Raise a KeyError if key is not in the hash table.

        @:param self: the object
        :param key: Unique key corresponding to the Data in Value, serves as a unique identifier for the value
        @:return: none


        @pre-condition: Key exists in HashTable
        @post-condition: Key - Value pair in HashTable Deleted, and all items reinserted.
        @complexity: Worst-Case: O(n)
        @complexity: Best-Case: O(1)

        """
        key = str(key)
        try:
            if not self.__contains__(key):  # Checking that Key exits in HAshTable, else raise KeyError
                raise KeyError
        except Exception:
            raise KeyError(" Key to be deleted not found ")


        position = self.hash(key) #find position of key in HashTable

        key_present = False

        for _ in range(self.table_capacity):
            if self.array[position] is not None:
                if key == self.array[position][0]:
                    break
                else:
                    position = (position + 1) % len(self.array)
            else:
                break

        self.array[position] = None  # Set position to None
        self.count -= 1  # Subtract 1 from count
        position = (position + 1) % len(self.array)


        while self.array[position] is not None:         # Add all itmes afte the key back into the Array
            key = self.array[position][0]
            value = self.array[position][1]

            self.count -= 1
            self.array[position] = None
            self.insert(key, value)

            position = (position + 1) % len(self.array)

# z = HashTable()
# for i in range(50):
#     if (z.hash(i) == 0):
#         print(i)

# 7
# 16
# 28
# 41

# for i in [7,16,28,41]:
#     z[i] = i
#     print(z.count)
# print(z.array)
# print(z.count)
# print("\n\n\n")
# # z.delete(28)
# for i in [7,16,28,41]:
#     z.delete(i)
#     print(z.count)
# print("\n\n\n")
# print(z.count)
# print(z.array)


# z = HashTable()
# for i in range(11):
#         z.insert(i,i)
# print(z.array)
# z[10] = "hell"
# print(z.array)

