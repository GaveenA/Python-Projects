class Stack:
    def __init__(self, size=10):  # default size set to 10
        """Creates stack if size > 0."""
        if size <= 0:
            raise Exception("size must be positive")
        self.the_array = [None] * size
        self.top = -1

    def size(self):
        """Returns size, - the number of elements in self """
        return self.top + 1

    def is_empty(self):
        """Returns True if the stack is empty."""
        return self.size() == 0

    def is_full(self):
        """Returns True if the stack is full."""
        return self.size() >= len(self.the_array)

    def push(self, item):
        """adds item to the top of the stack if the stack is not full, or raises an Exception if its full """
        if self.is_full():
            raise Exception("The stack is full")
        self.top += 1
        self.the_array[self.top] = item

    def pop(self):
        """ Removes the top element of the stack and returns it , or raises an Exception """
        if self.is_empty():
            raise Exception("The stack is empty")
        item = self.the_array[self.top]
        self.the_array[self.top] = None
        self.top -= 1
        return item

    def reset(self):
        """ removes all items in Stack List """
        while not self.is_empty():
            self.pop()
        assert self.is_empty

