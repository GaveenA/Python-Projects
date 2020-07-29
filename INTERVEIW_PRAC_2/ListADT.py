#!/usr/bin/python3
class ListADT:

    def __init__(self, size=10):
        """
        This method is defined such that the user is allowed to provide the size upon creation.
        If they do not provide size, a default value of 10 is set.

        @:param self : the object
        @:param size: size of list
        @:return None
        @Pre Condition: size should be positive integer
        @Post Condition: array is created default size if size not provided.
        @complexity: Best case O(1), Worst case O(1)

        """
        self.the_array = [None] * size      # Creating  Array
        self.length = 0                     # Length of List  (initially set to 0)
        self.size = size                    # Length of Array


    def __str__(self):

        """
        This method returns a string representation of the list with one item per line.
        Method returns an empty string if the list is empty.

        @:param self: the object
        @:return String containing the items of the list or returns the empty string if the list is empty
        @Pre Condition: None
        @Post Condition: string representation of the list with one item per line.
        @complexity: Best case O(n), Worst case O(n) where n is length of string
        """

        string = ""
        if self.is_empty():                             # Check if string empty and return empty string
            return string
        for i in range(self.length):
            string += str(self.the_array[i]) + "\n"     # adding all elements of list to string
        return string                                   # Returns string representation of list

    def __len__(self):

        """
        The Method returns the length of the list, that is, the number of elements in the list.
        The method returns 0 if the list is empty.

        @:param self: the object
        @:return Number of elements in the list or 0 if the list is empty.
        @Pre Condition: None
        @Post Condition: 0 or positive integer
        @complexity: Best case O(1), Worst case O(1)
        """

        return self.length                  # return Length of list

    def __getitem__(self, index):

        """
        The Method Returns the item at index in the list, if index is non-negative.
        The function raises an IndexError if index is out of the range -len(self) to len(self)-1.
        If index is negative the method will return item at the end of the list (if index = -1)
        and returns item at the second-to last position (if index is -2) and so on.

        @:param self: the object
        @:param index: the position of the required element in the list
        @:return Element at index in the list
        @Pre Condition: index should be an positive integer, index < list of  length
                        if index negative integer , index >= -self.length
        @Post Condition: specific element in the list at index
        @complexity: Best case O(1), Worst case O(1)
        """

        if index < -self.length or index > self.length - 1:  # Checks if index is within valid range,
            raise IndexError('Index out of range')          # otherwise raise exception
        if index < 0:
            index = self.length + index                     # Convert negative index to positive
        return self.the_array[index]                        # Returns item at index


    def __setitem__(self, index, item):
        """
        Sets the value at index in the list to be item.
        The index can be negative, behaving as described above.
        Raises an IndexError if index is out of the range - len(self) to len(self) - 1.

        @:param self: the object
        @:param index: the value at index in the list to be item.
        @:param item: the value to be set at index in the list
        @:return None
        @Pre Condition: index should be an positive integer, index < list of  length
                        if index negative integer , index >= -self.length
        @Post Condition: new element on the list in that index
        @complexity: best case O(1), worst case O(1)

        """
        if index < -self.length or index > self.length - 1:     # Checks if index within the valid range,
            raise IndexError('Index out of range')              # otherwise raise exception
        if index < 0:
            index = self.length + index                         # Convert negative index to positive
        self.the_array[index] = item                            # Element at index = item

    def __eq__(self, other):

        """
        This method returns True if the list is equivalent to other.
        Takes into consideration if they have exactly the same elements in the same order.

        @:param self: the object
        @:param other: Secondary list which is compared against the List
        @:return True / False
        @Pre Condition: 'other' should be of type list
        @Post Condition: return True / False
        @complexity: Best Case O(1) when they are not equal, Worst Case O(n) - (n is length of string)
         """
        equal = True
        if self.length == len(other):           # Check if length of self = length of other
            for i in range(len(other)):         # proceed to check if individual elements of self equal to other
                if self.the_array[i] != other[i]:
                    return not equal            # if self not equal to then returns false

        else:
            return not equal                    # if self not equal to then returns false

        return equal                            # if self equals to other returns true

    def insert(self, index, item):
        """
        This method inserts item into the list at position index, shuffling the other items of the list
        accordingly, provided that the index is non-negative.
        If index is negative the method will add item to the end of the list (if index = -1)
        and to the second-to last position (if index is -2) and so on.

        IndexError raised if index is out of the range from -len(self)-1 to len(self).

        @:param self: the object
        @:param index: Position of the list into which the item is to be added
        @:param item: New element which is to be added to the list at index
        @:return None
        @Pre Condition: index should be an positive integer, index < list of  length
                        if index negative integer , index >= -self.length
        @Post Condition: element is added to index in the List, and the element at i and all elements ahead of i  moved one space forward
        @complexity: Best Case O(n), Worst Case O(n) - (n is the difference between length of list and index + 1)
        """
        if index < -self.length or index > self.length:         # Checks if index is within valid range,
            raise IndexError("Index out of range")              # Otherwise raise exception
        if self.is_full():
            raise Exception(" List is Full ")                   # Raise exception if self full
        if index < 0:
            index = self.length + index+1                       # Convert negative index to positive
        self.shift_right(index)                                 # Shuffles elements right
        self.the_array[index] = item                            # Insert item at index
        self.length += 1                                        # increments length of list

    def delete(self, index):
        """
        Returns the item at index from the list and deletes it,
        shuffling all items after it towards the start of the list.
        If index is negative the method will delete item at the end of the list (if index = -1)
        or delete the item at second-to last position (if index is -2) and so on.

        Raises IndexError if index is out of the range from -len(self) to len(self).

        @:param self: the object
        @:param: index: Position of the list containing the item to be deleted
        @:return output: the deleted item
        @Pre Condition: index should be an positive integer, index < list of  length
                        if index negative integer , index >= -self.length
        @Post Condition: element at the index is deleted and the elements at [i+1] and ahead are shifted once space back.
        @complexity: Best case O(n), Worst case O(n) - (n is difference between length of list and index - 1)
        """

        if index < -self.length or index >= self.length:        # Checks if index is within valid range,
            raise IndexError('Index out of range!')             # Otherwise raise exception

        if self.is_empty():
            raise Exception("List is already Empty")            # Raise exception if self empty

        if index < 0:
            index = self.length + index                         # Convert negative index to positive

        item = self.the_array[index]                            # Store value at index as item (to be deleted)
        self.shift_left(index + 1)                              # Shuffle List Left
        self.the_array[self.length - 1] = None                  # Set Last Element as None
        self.length -= 1                                        # decrement length of list
        return item                                             # Return deleted item

    def shift_left(self, index):
        """
        Shift items in the list starting at (and including)
        the given index towards the left (i.e. the start) of the list

        @:param self: the object
        @:param index: index at which the leftward shift starts
        @:return None
        """
        for i in range(index, self.length, +1):
            self.the_array[i - 1] = self.the_array[i]

    def shift_right(self, index):
        """
        Shift items in the list starting at (and including)
        the given index towards the right (i.e. the end) of the list

        @:param self: the object
        @:param index: index at which the rightward shift starts
        @:return None
        """
        for i in range(self.length - 1, index - 1, -1):
            self.the_array[i + 1] = self.the_array[i]

    def is_empty(self):
        """
        Returns True if and only if the list is empty.

        @:param self: the object
        @:return Boolean:  True / False
        @Post Condition: Return True / False
        @complexity: Best case O(1), Worst case O(1)
        """
        return self.length == 0

    def is_full(self):
        """
        Returns True if and only if the list is full.

        @:param self: the object
        @:return Boolean:  True / False
        @Post Condition: Return True / False
        @complexity: Best case O(1), Worst case O(1)
        """
        return self.length == len(self.the_array)

    def __contains__(self, item):
        """
        This Method checks if the required item is present in the List and returns True or False.

        @:param self: the object
        @:param item: The item whose presence in the list is tested.
        @:return Boolean:  True / False
        @Pre Condition: item can be of any type
        @Post Condition: Return True / False
        @complexity: Best case O(1) (item is at index 0)     Worst case O(n) -  (n represents length of string)
        """
        for i in range(self.length):
            if item == self.the_array[i]:   # Check each element of list to item
                return True                 # If one match found Return true
        return False                        # Otherwise return false

    def append(self, item):
        """
        This method adds element "item" to the end of the list

        @:param self: the object
        :param item: The element to be added to the end of the list
        :return: None
        @Pre Condition: item can be of any type
        @Post Condition: item added as the last element of list,    index = self.length
        @complexity: Best case O(1), Worst case O(1)
        """
        if not self.is_full():
            self.the_array[self.length] = item      # Add item to end of list if list not full
            self.length += 1                        # Incrementing length of list
        else:
            raise Exception('List is full')         # if list full raise exception

    def unsafe_set_array(self, array, length):
        """
        UNSAFE: only to be used during testing to facilitate it!! DO NOT USE FOR ANYTHING ELSE
        """
        try:
            assert self.in_test_mode
        except:
            raise Exception('Cannot run unsafe_set_array outside testing mode')

        self.the_array = array
        self.length = length

