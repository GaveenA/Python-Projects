from task6_HashTable import HashTable
import string

class Freq:




    def __init__(self):
        """
        Creates a new hash table, with initial table capacity 11,
        and using base, 31 for the hash function (see hash below).



        @:param self: the object
        @:return: Return None

        @complexity: Worst-Case: O(1)
        @complexity: Best-Case: O(1)

        """
        self.hash_table = HashTable(11, 31)
        self.most_common_word = ""
        self.max = 0




    def add_file(self, filename):

        """
        Reads each word from the file into the hash table, in such a way that the data associated to the word
        is its “occurrence count”, i.e., the number of times the word has been “added” to the hash table
        (which is the same as the number of times it has already appeared in the file).
        The class (and its methods) keep track of the number of occurrences max for the most common word read.

        :param self: the object
        :param filename: The File to be read
        :return: none

        @pre-condition: the filename must be valid, else throws an exception
        @post-condition: Converts all words to lowercase, removes whitespace, Strips punctuation from all words and then adds to hash_table, with occurrence count.
        @complexity: Worst-Case: O(1)
        @complexity: Best-Case: O(1)
        """


        try:
            myfile = open(filename, "r", encoding="utf8")
        except FileNotFoundError:
            raise FileNotFoundError("File does not exist")

        exclude = set(string.punctuation)     #loading puntuation
        exclude.add('"')
        exclude.add('“')
        exclude.add('”')

        lines = myfile.readlines()
        for line in lines:
            for word in line.split():  #removing whitespace
                word = word.lower()     #converting to lowercase
                word_stripped_punct = ''.join(char for char in word if char not in exclude)  # Removing exclude from words

                if not word_stripped_punct in self.hash_table:
                    self.hash_table[word_stripped_punct] = 1     # Setting value (in key-value pair) to be the occurrence count
                else:
                    count = self.hash_table[word_stripped_punct]     # Recaling the value in key-value pair (representing occurrence count)
                    self.hash_table[word_stripped_punct] = count + 1 # incrementing the occurrence count
                if self.hash_table[word_stripped_punct] > self.max:  #Checks if count > self.max:
                    self.max = self.hash_table[word_stripped_punct]
                    self.most_common_word = word_stripped_punct
        myfile.close()


    def rarity(self, word):
        """
        Given a word, this function returns its rarity score.

        Any word that appears at least max/100 times is considered to be common (score 0).
        Any word that appears less than max/1000 times is considered to be rare (score 2).
        Any word in between (less than max/100 and greater or equal to max/1000) is considered to be
        uncommon (score 1).
        Any word which has never been observed is a misspelling (score 3).

        :param self: the object
        :param word: the word whose rairity score is to be checked
        :return: the rarity score - (0, 1, 2, 3)

        @post-condition: return 0, 1, 2, 3
        @complexity: Worst-Case: O(1)
        @complexity: Best-Case: O(1)


        """

        if word not in self.hash_table:     # Any word which has never been observed is a misspelling (score 3)
            return 3
        if self.hash_table[word] >= self.max/100: # Any word that appears at least max/100 times is considered to be common (score 0)
            return 0
        if self.hash_table[word] < self.max/1000: # Any word that appears less than max/1000 times is considered to be rare (score 2)
            return 2
        if self.max/1000 <= self.hash_table[word] < self.max/100: # Any word in between (less than max/100 and greater or equal to max/1000) is considered to be uncommon (score 1).
            return 1





#Testing Harness

# x = Freq()
# x.add_file("testfile_task6.txt")
#
#
# print(x.hash_table.array)
#
# print(x.hash_table["a"])
# print(x.rarity("a"))
# print("\n\n")
#
# print(x.hash_table["b"])
# print(x.rarity("b"))
# print("\n\n")
#
# print(x.hash_table["c"])
# print(x.rarity("c"))
# print("\n\n")
#
# print(x.hash_table["d"])
# print(x.rarity("d"))
# print("\n\n")
#
# print(x.hash_table["e"])
# print(x.rarity("e"))
# print("\n\n")
#
# print(x.rarity("z"))
# print("\n\n")
# print(x.max)
