class TrieNode:
    """
    TrieNode class represents the nodes of the Prefix Trie
    """
    def __init__(self):
        """
        Initialize the variables upon creation of the node
        """
        self.children = [None] * 26     # There are 26 child arrays in a TrieNode(), each representing a letter in the english alphabet

        self.endOfWord = False      # This key represents that the Node is a leaf node
        self.songID = []            # Holds the songID's of the songs in which the word appears in (songID's appended when the leaf node is reached)
        self.char_appear_songID = []    # Holds the songID's of the songs in which the character substring appears in (songID's appended after insertion of each character)



class PrefixTrie:
    """
    This class holds the methods of the Prefix Trie class
    """

    def __init__(self):
        """
        Initialize the root node as a TrieNode() object
        """
        self.root = TrieNode()


    def letterToIndex(self, char):
        """
        This function converts characters to the relevant index in the alphabet
        where 'a' has index 0 and 'z' has index 25

        :param char: the character to be converted into correct index of alphabet
        :return: index
        """
        index = ord(char) - ord('a')     # Convert character into index
        return index


    def insert(self, word, songID):
        """
        This function adds the 'word' which is a string, character by character into the PrefixTrie,
        this is done by iterating over each character in the 'key' and if that character substring is not present in the
        PrefixTrie a new TrieNode is created and the char_appear_songID list is updated. The 'CurrentRoot' is updated after each iteration.
        As we iterate over the characters in the 'key', if that combination of character substring is already present in the Prefix Trie
        the SongID is appended to the char_appear_songID list of the currentRoot (provided it is not already present).
        At the completion of the addition of the 'word' to the prefix trie, when the leaf node is reached, the songID is appended to the
        songID list of the leafNode and the boolean 'endOfWord' is set to True

        :param word: the string to be added to the prefix trie
        :param songID:
        :return: None

        Best-case Time Complexity: O(n) where n is the lenth of input into the prefix trie
        Worst-case Time Complexity: O(n) where n is the lenth of input into the prefix trie
        """

        word=str(word.lower())    # Coverting to Lower case

        valid = True
        for letter in word:      # Checking if all the characters in the 'key' are alphabet characters
            if (ord(letter) - ord('a')) >=0 and (ord(letter) - ord('a')) <=26:
                continue
            else:
                valid = False
                break


        if valid == True :
            currentRoot = self.root
            for letter in range(len(word)):          # Iterating over all the characters in the 'key', and if the character is not present, addded to the prefix trie
                index = self.letterToIndex(word[letter])     # Converting the character to the correct index, where 'a' has index 0 and 'z' has index 25

                if not currentRoot.children[index]: # If the character is not present in the currentRoot.children, create new TrieNode at the correct child index
                    currentRoot.children[index] = TrieNode()
                    currentRoot = currentRoot.children[index]   # Setting the currenntRoot to the node of the current character

                    # In this If-Else Block we update the character substring List by appending the songID to thr list, provided it is not already present
                    if len(currentRoot.char_appear_songID) != 0:
                        if currentRoot.char_appear_songID[-1] != songID:
                            currentRoot.char_appear_songID.append(songID)
                            # print(len(currentRoot.char_appear_songID))
                    else:
                        currentRoot.char_appear_songID.append(songID)
                        # print(currentRoot.char_appear_songID)
                        # print(len(currentRoot.char_appear_songID))


                else:               # If the character is already present in the tree in the correct order of character subsrings
                    currentRoot = currentRoot.children[index]   # Update the currentRoot to currentRoot.children[index]

                    # In this If-Else Block we update the character substring List by appending the songID to thr list, provided it is not already present
                    if len(currentRoot.char_appear_songID) != 0:
                        if currentRoot.char_appear_songID[-1] != songID:
                            currentRoot.char_appear_songID.append(songID)
                            # print(currentRoot.char_appear_songID)
                            # print(len(currentRoot.char_appear_songID))
                    else:
                        currentRoot.char_appear_songID.append(songID)
                        # print(currentRoot.char_appear_songID)

            currentRoot.endOfWord = True            # If the leaf node is reached, the end of the word is reached and songID is appended to the SongID list
            if len(currentRoot.songID) != 0:
                if currentRoot.songID[-1] != songID:
                    currentRoot.songID.append(songID)
            else:
                currentRoot.songID.append(songID)
        else:
            raise Exception("Enter valid lowercase word as Key")        # If the word is invalid, not alphabetical characters, raise exception


    def search(self, word):
        """
        This function checks for the presence of a word in a prefixTree and returns the SongIDs of the songs in which the word can be found in.
        The function iterates over the characters of the word and at each iteration checks for the presence of the character in the prefix trie
        in that order, if the character is found in the correct order in the prefix trie the currentRoot is moved to that Node.
        When the end of the word is reached, we return the list of the SongIDs at that leaf node.

        :param word: The word for whose presence in the Prefix Trie is searched
        :return: List of SongID's of the songs in which the word is appearing in
        Best-case Time Complexity: O(n) - Where n is the length of the word being searched
        Worst-Case Time Complexity: O(n) - Where n is the length of the word being searched
        """
        currentRoot = self.root     # Current root set as self.root

        for letter in range(len(word)):     # iterating over all characters in the word
            index = self.letterToIndex(word[letter])        #   Converting the character to correct index
            if currentRoot.children[index] == None:     # If the character is not present at currentRoot.children[index]: return Not Found
                list = ["Not Found"]
                return list
            currentRoot = currentRoot.children[index]           # If the character is found,  update the current root

        if currentRoot.endOfWord == True:       # If the end of the word is reached (leaf node): return the songID list
            # print(currentRoot.word)
            if len(currentRoot.songID) > 0:     #
                return currentRoot.songID
            else:
                list = ["Not Found"]
                return list
        else:
            list = ["Not Found"]
            return list


    def retreive_char_appear_count(self, currentRoot):
        """
        This function returns the index of the child where that substring has the most appearances in songs
        This is done by iterating ove the 26 child nodes of the current root and checking which child node has
        the most number of songs in which that sub-string appears in.

        :param currentRoot: The node whose child nodes are being explored
        :return: the index of the child node with most number of songs in which that character sub-string appears in.
        best-case time complexity: 0(1)
        worst-case time complexity: O(1)
        """
        max = -2        # Max is initialized
        index = 0   # Index is initially set to 0

        for i in range(26):     # Iterating over the 26 child nodes
            if currentRoot.children[i]:     # If valid child node which is not None, proceed, else continue to next iteration
                if len(currentRoot.children[i].char_appear_songID) > max:
                    max = len(currentRoot.children[i].char_appear_songID)       # Update Max as nessesary
                    index = i                                                   # Updating index
                else:
                    continue
            else:
                continue
        #print(chr(ord('a')+index))
        return index        # Return index





    # def recursive_find_most_common(self, currentRoot,string):
    #     if currentRoot.endOfWord:
    #         index = self.retreive_char_appear_count(currentRoot)
    #         if currentRoot.children[index]:
    #             string += chr(ord('a') + index)
    #             return self.recursive_find_most_common(currentRoot.children[index],string)
    #         else:
    #             #print(string)
    #             return str(string)
    #     else:
    #         index = self.retreive_char_appear_count(currentRoot)
    #         string += chr(ord('a')+index)
    #         #print(string)
    #         return self.recursive_find_most_common(currentRoot.children[index],string)



    def recursive_find_most_common(self, currentRoot, string):
        """
        This function iterates recursively to find the most common word given a currentRoot which is the
        end node of a prefix in the prefix Tree. This function is called by an external function which determines the end node
        of the prefix in the prefix tree, then proceeds to call this fucntion (recursive_find_most_common) providing the
        end node of the prefix as 'currentNode'.
        This function will then continuously recurse to find a word derived from that prefix which occurs in the most songs.

        :param currentRoot: The end node of the prefix which is found by the calling function the passed as an argument to this function
        :param string: the string which is updated at each level of recursion with the character with most song occurances at that level,
               to eventually create the word with most song occurrences.
        :return: Return the word, derived from the prefix, which occurs in the most songs.

        best-case time complexity: 0(m) where m is the length of the string returned
        worst-case time complexity: 0(m) where m is the length of the string returned
        """

        if currentRoot.endOfWord: # Checking if the current root is a leaf node
            index = self.retreive_char_appear_count(currentRoot)
            if currentRoot.children[index]:     # Checking if the children nodes exist
                if len(currentRoot.char_appear_songID)<len(currentRoot.children[index].char_appear_songID): # Checking if the child node has more occurances than the parentNode
                    string += chr(ord('a') + index)     # IF so, the string is appended with the next character and the function is called again
                    return self.recursive_find_most_common(currentRoot.children[index], string)     # Function called again with currentRoot attribute set as currentRoot.children[index]
                else:
                    return str(string)  # If no more child nodes exist, we have reached the end of the word with most common occurances
            else:
                # print(string)
                return str(string)
        else:   # If not a leaf node
            index = self.retreive_char_appear_count(currentRoot)    # Find index of child node (character) which appears in most songs
            string += chr(ord('a') + index)     # Append the character into the string
            # print(string)
            return self.recursive_find_most_common(currentRoot.children[index], string)     # Function called again with currentRoot attribute set as currentRoot.children[index]




    def most_common_search(self, prefix):
        """
        This function finds and returns the word that occurs in most songs, which is derived from the prefix

        :param prefix: The prefix for which the function finds the word with most occurrences in songs
        :return: The word in prefixTrie derived from the prefix, with most occurences in words
                 else:
                "Not Found" if there is no word which matches the prefix
        best-case time complexity: O(m) where m is the length of the word that occurs in most songs derived from prefix
        worst-case time complexity: O(m) where m is the length of the word that occurs in most songs derived from prefix
        """

        found = True
        currentRoot = self.root     # Set the currentRoot as root
        for letter in range(len(prefix)):       # Iterating over the characters in prefix to move currentRoot to correct node
            index = self.letterToIndex(prefix[letter])

            if not currentRoot.children[index]:     # If a character in prefix is not present in the prefixTrie; break out and return Not Found
                found = False
                break
            else:
                currentRoot = currentRoot.children[index] # Else; update the currentRoot to the correct node

        string = ""
        if found == True:
            sub_str = self.recursive_find_most_common(currentRoot,string)       # Call function to find the word with highest frequency.
            #print(sub_str)
            return (prefix + sub_str)
        else:
            return "Not Found"




def lookup(data_file, query_file):
    """
    Given a file of song lyrics and a file of queries, this function finds which songs contain the words in the query file

    The function takes as input two filenames, and for each word in query_file determines the songs which contain that word.
    lookup will write output to a file named "song_ids.txt".

    This file will contain the same number of lines as query_file. If the word on line i of query_file appears in at
    least one song, then line i of "song_ids.txt" will contain the song IDs (in ascending order, separated by spaces)
    that contain that word. If the word does not appear in any song, then the corresponding output line should
    be the string "Not found".

    :param data_file: The file containing songs
    :param query_file:  The File containing the query's
    :return: None

    Time-complexity:

    CI is the number of characters in data_file
    CQ is the number of characters in query_file
    CP is the number of characters in song_ids.txt
    """

    file = open(data_file, 'r')
    tuples = []

    for line in file:

        index_colon = line.index(':')

        id = line[0:index_colon]

        new_line = line[index_colon + 1:]
        new_line = new_line.split()

        for word in new_line:
            tuples.append((word, id))
        # print(tuples)
    file.close()

    file2 = open(query_file, 'r')
    query_array = file2.read().splitlines()
    file2.close()


    t = PrefixTrie()
    for elem in tuples:
        t.insert(elem[0],elem[1])



    file = open("song_ids.txt", 'w')

    for word in query_array:
        line = str(t.search(word))
        newline = line[1:-1]
        file.write(newline)
        file.write('\n')
    file.close()





def most_common(data_file, query_file):
    """
    This function determine which word is present in the most songs and begins with that prefix.
    most_common will write to a file “most_common_lyrics.txt”.
     This file will contain the same number of lines as query_file.
     If the string on line i of query_file is the prefix of a word in any song, then line i of “most_common_lyrics.txt” will contain the word which ...
        a) Is present in the most songs
        b) Has the string on line i of query_file as a prefix
    If the string on line i of query_file is not the prefix of any word in any song, then the corresponding output line should be the string "Not found".

    :param data_file: The file containing songs
    :param query_file:  The File containing the query's
    :return: None

    Time-complexity:

    CI is the number of characters in data_file
    CQ is the number of characters in query_file
    CM is the number of characters in most_common_lyrics.txt

    """

    file = open(data_file, 'r')
    tuples = []

    for line in file:

        index_colon = line.index(':')

        id = line[0:index_colon]

        new_line = line[index_colon + 1:]
        new_line = new_line.split()

        for word in new_line:
            tuples.append((word, id))
        # print(tuples)
    file.close()

    file2 = open(query_file, 'r')
    query_array = file2.read().splitlines()
    file2.close()


    t = PrefixTrie()
    for elem in tuples:
        t.insert(elem[0],elem[1])

    file = open("most_common_lyrics.txt", 'w')

    for word in query_array:
        result = t.most_common_search(word)
        #print(result)
        file.write(str(result))
        file.write('\n')
        #print("\n\n"+result)
    file.close()





def palindromes_aux(string):
    """
    THis function is used to find the indexes of palindromic substrings of a string.
    :param string: The string for which we search the palindrome substrings
    :return: Idexes of the palidrome substrings

    """
    palidromes = []

    for i in range(len(string)):

        for j in range(len(string)):
            if i+j<len(string) and i-j>=0:
                if string[i+j] == string[i-j]:
                    palidromes.append(((i-j,i+j),string[i-j:i+j+1]))
                else:
                    break
            else:
                break

    for i in range(len(string)):
        for j in range(len(string)):
            if i+j+1 < len(string) and i - j >= 0:
                if string[i+j+1] == string[i - j]:
                    palidromes.append(((i - j, i+j+1), string[i - j:i + j + 1+1]))
                else:
                    break
            else:
                break
    return palidromes


def palindromic_substrings(string):
    """
    THis function is used to find the indexes of palindromic substrings (of length 2 or greater) of a string.
    :param string: The string for which we search the palindrome substrings
    :return: Idexes of the palidrome substrings, of length 2 or greater.
    """

    palidromes = palindromes_aux(string)
    valid_palindrome_indexes = []

    for elem in palidromes:
        if len(elem[1]) > 1:
            valid_palindrome_indexes.append(elem[0])
            # print(f"{elem[1]}   {elem[0]}")

    return valid_palindrome_indexes







if __name__ == "__main__":
    lookup('songs.txt','example_queries.txt')

    most_common('songs.txt','query_task2.txt')

    print(palindromic_substrings("ababcbaxx"))


