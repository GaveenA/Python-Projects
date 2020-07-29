


#_______________________________________________________________________________________________________________________

# Task 1


def process(file):

    """
    We start with a "file" containing lyrics from many songs.
    The function takes as input a string of a filename
    The function will sort the words of all the songs, and output these sorted words to another file.

    A word is defined to be a sequence of lowercase English characters (a-z).
    A word does not contain any kind of punctuation or other symbols.
    Song lyrics are a sequence of words separated by spaces.
    Each line of the input file will start with a non-negative integer, which is the song ID.
    This number is followed by a colon, then the song lyrics on a single line

    process will write output to a file named "sorted_words.txt" (which it will create).
    This file will consist of T lines, where T is the total number of words over all songs in the input file.
    Each line will start with a word, then a colon, and then the song ID of the song that word belongs to.
    The order of the lines depends on the words. If the word in line x is lexicographically less than
    the word in line y, then x will appear before y in sorted_words.txt. If two line have the same word,
    then the one with lower song ID will appear first.

    Algorithm Walk-through:

    The function process(filename) starts off by reading in the lines of 'file' into a list of 'tuples' of word-ID pairs.
    This is done by using slice and the index of the colon(:) to split the song ID and corresponding Word.
    We then build the list of tuples by appending a tuple consisting of word and corresponding ID into a list called "tuples'.
    I then used the function 'maxDigitVal' which runs in complexity O(N). This function 'maxDigitVal'
    gets the length of the longest first element in the list of tuples by iterating over all the first elements (word) of
    the list of tuples and finding the longest word.

    We then use the padding approach to bring all the words in the list of tuples to the length of the longest word.
    This is done with time complexity O(TM) where T is the length of the longest word and M is the number of words we are iterating over.
    This is done so that radix sort an be done on the list of tuples, to sort the list by the words alphabetically.
    We do the padding by iterating over all the elements in the list of 'tuples', and if the word in each tuple (first element of each tuple)
    is less in length compared to the longest word, that difference in length is added in zeros ('0' - padding element)to the end of that particular word by means of string concatenation.
    We then have a list of 'tuples' which where each tuple contains a word (first element) that is of the length of the longest word.

    We then sort the list of tuples using radix sort, to sort the tuples by the alphabetical order of the words.


    How Radix Sort works:
    In this variant of radix sort is least significant digit (LSD) radix sort.
    In essence, LSD radix sort works by sorting an array of elements
    one digit at a time, from the least significant to the most significant. Each digit is sorted in a
    stable manner in order to maintain the relative ordering of the previously sorted digits.

    We sort the array one digit at a time, from least significant (rightmost column) to most significant (leftmost column)

    For each digit: We sort using a stable sorting algorithm, this is done im Radix Pass

    Radix Sort Works with complexity (best/worst case ): O(KN) -  where K is the length of the longest element in list and N is the length of the list




    How Radix Pass Works:
    Suppose we wish to sort an array that contains only elements in some fixed universe U .
    The radix pass algorithm sorts the words based on the positions of digits column wise by taking their corresponding
    ascii values into considerations (ascii value obtained using getDigit which is used in thr function).

    Specially in the context of the function process(), let’s assume that all of the words are in the range of the alphabet
    Thus taking into consideration the range of ascii values that the words may occupy (ascii value of z = 122) we
    provide appropriate base for radix_pass to function correctly.

    We do a pass over the input to count the number of occurrences of each ascii value
    In order to preserve the stability of the algorithm we then do a second pass over the input
    and place each element into its correct position.

    Radix Pass works with complexity (best/ worst case):  O(n + u )  where n is the length of the longest string and u is the base

    The function radix sorted returns a list of tuples where the words (first elements of tuples) are sorted alphabetically.
    This 'sorted_list' now must be depadded whereby the padding element('0') must be removed from all the words to which it was added.
    This is done with time complexity O(TM) where T is the length of thr longest word and M is the number of words we are iterating over.
    We do the depadding by iterating over the tuples in 'sorted_list' and for each word (first element in tuple) we find the index of the
    'padding element' which is '0'. Using this index (of padding element) we use slice to find the original word, and the original word added back into the tuple at the
    same position (padded word replaced with original word).

    We then have to sort the identical words by song_ID. whereby if the words are same, the word with the smaller song_ID appears first.
    This is done by running a function 'second_sort' which sorts the duplicate words by Song ID using radix_sort_integers (refer Code)
    The second sort function runs with complexity O(KN) - where K is the length of ID's for each word and N is the length of thr list of tuples containing unique words and corresponding ID's

    We open a file "sorted_words.txt"
    Finally we iterate over each tuple in the list of sorted tuples and for each tuple the word (first element) and song ID (second element)is written into the file.
    The file will contain only one word and song ID per line.






    :param file: contains song ID and lyrics of corresponding song, seperated by a colon.
    :return: None - writes the words of each song and corresponding song ID into a file "sorted_words.txt"

    :pre-condition: file should contain the song ID and the corresponding song lyrics seperated by a colon

    :post-condition: the file sorted_words.txt contains individual song lyrics (words) and corresponding song ID's
                     separated by a colon. Note that The order of the lines depends on the words. If the word in line x
                     is lexicographically less than the word in line y, then x will appear before y in sorted_words.txt.
                     If two line have the same word, then the one with lower song ID will appear first.
    :worst-case time-complexity:
    :best-case time-complexity:

    """

    # appending the Song ID and each word into an array of tuples

    file = open(file, 'r')
    tuples = []

    for line in file:

        index_colon = line.index(':')

        id = line[0:index_colon]

        new_line = line[index_colon+1 :]
        new_line = new_line.split()

        for word in new_line:
            tuples.append([word, id])
        #print(tuples)
    file.close()





    maxLength = maxDigitVal(tuples)     # Finding the length of the longest lyric (word)


    # To ensure all words are of the length of the longest word (lyric) we take padding approach by concatenating all
    # words shorter than the longest word with a '0'

    for element in tuples:
        if len(element[0]) < maxLength:
            difference = maxLength - len(element[0])
            element[0] = str(element[0])+ str(0)*difference

    sorted_list = radix_sort(tuples)        # Sorting the padded words with radix_sort

    for element in sorted_list:             # Removing the Pad (" 0" ) from padded words
        try:
            index_of_pad = element[0].index('0')
            element_without_pad = element[0][0: index_of_pad]
            element[0] = element_without_pad
        except:
            element[0] = element[0]

    final_sorted_list = second_sort(sorted_list)

    file = open("sorted_words.txt", 'w')            # Writing to a file.
    for i in range(len(final_sorted_list)):
        file.write(final_sorted_list[i][0] + ':' + str(final_sorted_list[i][1]) + '\n')
    file.close()











def getDigit(word, digit):

    """
    The purpose of this function is to return the ascii value of the digit of the word (given in parameter)

    :param word: The word for which the digit(element) is seeked
    :param digit: The element of the word whose ascii value we are returning at the termination of function
    :return: the ascii value of the digit (of the word)
    :pre-condition: The digit (element of word) must be whithin the length of the word itself, if not we return the ascii value of zero.
    :post-condition: The ascii value of the digit is returned.
    :worst-case time-complexity: O(N)
    :best-case time-complexity: O(N)
    """

    number = str(word)
    if digit <= (len(number)):
        output = number[-digit]
        return ord(output)
    else:
        return ord("0")


def maxDigitVal(array):
    """
    This function gets the length of the longest element of the array

    :param array: The array whose longest element is found for
    :return: length of longest element in array
    :pre-condition: Input a list of tuples
    :post-condition: Returns the length of the longest element in array
    :worst-case time-complexity:O(N) where N is the length of the array
    :best-case time-complexity: O(N) where N is the length of the array
    """
    maxDigitVal = array[0][0]

    for i in range(1, len(array)):

        if len(str(maxDigitVal)) < len(str(array[i][0])):
            maxDigitVal = array[i][0]
    return len(str(maxDigitVal))



def radix_pass(lst, base, digit):

    """

    Suppose we wish to sort an array that contains only elements in some fixed universe U .
    The radix pass algorithm sorts the words based on the positions of digits column wise by taking their corresponding
    ascii values into considerations (ascii value obtained using getDigit which is used in thr function).

    Specially in the context of the function process(), let’s assume that all of the words are in the range of the alphabet
    Thus taking into consideration the range of ascii values that the words may occupy (ascii value of z = 122) we
    provide appropriate base for radix_pass to function correctly.

    We do a pass over the input to count the number of occurrences of each ascii value
    In order to preserve the stability of the algorithm we then do a second pass over the input
    and place each element into its correct position.

    :param lst: The list to be sorted
    :param base: The base is based on the the range of ascii values out list spans over.
    :param digit: The digit (columns) we are sorting the list by.
    :return: result: List sorted by digit(collumn)
    :pre-condition: Each element of the list must be a tuple, first element of the tuple must be a string
    :post-condition: List is sorted according to digit column of characters
    :worst-case time-complexity: O(n + u )  where n is the length of the longest string and u is the base
    :best-case time-complexity:  O(n + u )  where n is the length of the longest string and u is the base

    """
    u = (base)
    counter = [0] * u
    position = [0] * u
    result = [None] * len(lst)
    for i in range(len(lst)):
        # print(getDigit(lst[i][0], digit))
        counter[getDigit(lst[i][0], digit)] += 1
    # print(f"count is {counter}")

    for i in range(1, u):
        position[i] = position[i - 1] + counter[i - 1]
    # print(f"position is {position}")

    # print(f"position is {position}")
    # print(f"count is {counter}")
    # print("hello")

    for i in range(len(lst)):
        digit_recall = getDigit(lst[i][0], digit)
        # print(f"position again is {position}")
        result[position[digit_recall]] = lst[i]
        position[digit_recall] += 1
    # print(f"result is {result}")
    return result




def radix_sort(lst):

    """

    In this variant of radix sort is least significant digit (LSD) radix sort.
    In essence, LSD radix sort works by sorting an array of elements
    one digit at a time, from the least significant to the most significant. Each digit is sorted in a
    stable manner in order to maintain the relative ordering of the previously sorted digits.

    We sort the array one digit at a time, from least significant (rightmost column) to most significant (leftmost column)

    For each digit: We sort using a stable sorting algorithm, this is done im Radix Pass

    :param lst: Contains the list to be sorted
    :return: output_list: Return sorted output list (Sorted from from least significant (rightmost column) to most significant (leftmost column) )
    :pre-condition: Each element of the list must be a tuple, first element of the tuple must be a string
    :post-condition: List is sorted one digit at a time, from least significant (rightmost column) to most significant (leftmost column)
    :worst-case time-complexity: O(KN) -  K is the length of the longest element in list and N is the length of the list
    :best-case time-complexity: O(KN)  - K is the length of the longest element in list and N is the length of the list

    """

    output_list = lst

    longestNum = maxDigitVal(lst)
    # print(f" most digits in the list is {longestNum}")

    for digit in range(1, longestNum + 1):
        output_list = radix_pass(output_list, 123, digit)
        # print(f"result is {output_list} for digit {digit}")
    return output_list





def remove_duplicates(duplicate):

    """
    This function aims to remove duplicate tuples from a list called - "duplicate".
    This function outputs a list containing unique tuples.
    However, the output list may contain tuples that have one element of the tuple in common, but the other element being different.
    This is fine because each tuple is still unique, despite some tuples having one element in common.

    :param duplicate: List containing duplicate tuples,
    :return: final_list: A list of unique tuples.
    :pre-condition: Input Must be  a list.
    :post-condition: Returns a list of unique elements.
    :worst-case time-complexity: O(N) - where N is length of list containing duplicates
    :best-case time-complexity: O(N) -  where N is length of list containing duplicates

    """
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list



def check_duplicates(word, sublist):

    """
    This function checks for the presence of a "word" in a sublist by iterating through the first elements of a list of tuples
    in "sublist" and if a match is found for word, the second element of that tuple is added to a "id_list"
    The function then returns the id_list which contains a list of corresponding Song ID's of Songs which contain the word being searched.

    :param word: The word being searched for which corresponding ID's are found for.
    :param sublist: The list of tuples, the first element (0th index) of the tuples is iterated through to find a match for the word
    :return: id_list: List of ID's of Songs which contain the "word"
    :pre-condition: Each element of the list must be a tuple and first element of tuple contains word
    :post-condition: Return list of ID's of Songs which contain the "word"
    :worst-case time-complexity:O(N) Where N is the length of sublist
    :best-case time-complexity:O(N) Where N is the length of sublist

    """
    id_list = []
    for i in range (len(sublist)):
        if sublist[i][0] == word:
            id_list.append(int(sublist[i][1]))    # Converting ID to integer before appending to ID List
    return id_list



def second_sort(sorted_list):

    """

    This function iterates over the range of the "sorted_list" of tuples, given as input, and for each of the first elements of
    tuples, which contains a "word", we carry out check_duplicates which in turn returns a list of Song ID's containing that particular word.
    This list of song ID's is then sorted using radix_sort for integers.
    The "word" and corresponding sorted list of song ID's is them appended as a tuple to a list, and thr process repeats as the
    loop iterates for each of the first elements in the list of tuples in the "sorted_list"

    We then get a list - final_list which  contains a list of tuples where the first element of each tuple is the word and the second
    element of the tuples is a list of associated song ID's.
    We then iterate over the list of tuples containing word and asociated song ID's and run a second loop iterating over
    the list of ID's at each tuple, we finally create a new list of tuples containing word and ID.

    :param sorted_list: The list of tuples, in which for each of the first elements in the list of tuples a sorted list
                        of corresponding Song ID's is genersted
    :return: final_list: list of tuples each containing a word and the corresponding Song ID's (of the songs which contain the word )
    :pre-condition: Each element of the list must be a tuple and first element of tuple contains a word
    :post-condition: Returns list of tuples each containing a unique word and the corresponding Song ID's (of the songs which contain the word )
    :worst-case time-complexity: O(KN) - where K is the length of ID's for each word and N is the length of thr list of tuples containing unique words and corresponding ID's
    :best-case time-complexity: O(KN) - where K is the length of ID's for each word and N is the length of thr list of tuples containing unique words and corresponding ID's

    """
    words_ids_list = []
    final_list = []


    for i in range(len(sorted_list)):
        id_list = check_duplicates(sorted_list[i][0], sorted_list)
        id_list_sorted = radix_sort_integers(id_list)
        # print(id_list)
        # print(id_list_sorted)

        words_ids_list.append((sorted_list[i][0], id_list_sorted))

    words_ids_no_duplicates = remove_duplicates(words_ids_list)

    for i in range(len(words_ids_no_duplicates)):
        for j in range(len(words_ids_no_duplicates[i][1])):
            final_list.append( ( words_ids_no_duplicates[i][0], str(words_ids_no_duplicates[i][1][j]) ) )
    return final_list







def getDigit_of_Integers(integer, digit):
    """
    The purpose of this function is to return the value of the digit of the integer (given in parameter)

    :param integer: The integer for which the digit(element) is seeked
    :param digit: The element of the integer whose value we are returning at the termination of function
    :return: the value of the digit (of the integer)
    :pre-condition: The digit (element of integer) must be whithin the length of the word itself, if not we return the value zero.
    :post-condition: The value of the digit is returned.
    :worst-case time-complexity: O(N)
    :best-case time-complexity: O(N)

    """
    number = str(integer)
    if digit <= (len(number)):
        output = number[-digit]
        return int(output)
    else:
        return 0


def maxDigitVal_2(array):

    """
    This function gets the length of the longest element of the array

    :param array: The array whose longest element is found for
    :return: length of longest element in array
    :pre-condition: Input a list (not a list of tuples)
    :post-condition: Returns the length of the longest element in array
    :worst-case time-complexity:O(N)
    :best-case time-complexity: O(N)

    """
    maxDigitVal = array[0]

    for i in range(1, len(array)):

        if len(str(maxDigitVal)) < len(str(array[i])):
            maxDigitVal = array[i]
    return len(str(maxDigitVal))




def radix_pass_integers(lst, base, digit):
    """

    Suppose we wish to sort an array that contains only integers in some fixed universe U .
    Specially, let’s assume that all of the integers are in the range 0 to u − 1.
    We do a pass over the input to count the number of occurrences of each number.
    If we know that there are for example, one 0, two 1’s, one 2 and three 3’s
    then we can immediately deduce that the sorted array is 0,1,1,2,3,3,3 in linear time. Of course, simple naively
    writing out the output would not be a stable sort (indeed, any satellite data attached to the input is lost entirely),
    so we should instead do a second pass over the input and place each element into its correct position.
    - Reference 2004 Notes.


    :param lst: The list to be sorted based on digit
    :param base: The range of integers the list spans over (0 - 9)
    :param digit: the digit (collumn) we are sorting the list by
    :return: result: List sorted by digit(collumn)
    :pre-condition: The list given as input should be a list of integers.
    :post-condition: List is sorted according to digit column of characters
    :worst-case time-complexity: O(n + u )  where n is the length of the longest integer and u is the base
    :best-case time-complexity:  O(n + u )  where n is the length of the longest integer and u is the base

    """
    u = (base)
    counter = [0] * u
    position = [0] * u
    result = [None] * len(lst)
    for i in range(len(lst)):
        #print(getDigit(lst[i][0], digit))
        counter[getDigit_of_Integers(lst[i], digit)] += 1

    for i in range(1,u):
        position[i] = position[i - 1] + counter[i - 1]

    # print(f"position is {position}")
    # print(f"count is {counter}")
    # print("hello")

    for i in range(len(lst)):
        digit_recall = getDigit_of_Integers(lst[i], digit)
        # print(f"position again is {position}")
        result[position[digit_recall]] = lst[i]
        position[digit_recall] += 1
    #print(f"result is {result}")
    return result



def radix_sort_integers(lst):

    """
    This implementation of Radix sort for integers is non-comparison-based sort that achieves linear time
    for a wider class of inputs than counting sort.
    This function of radix sort is least significant digit (LSD) radix sort.
    In essence, LSD radix sort works by sorting an array of elements one digit at a time,
    from the least significant to the most significant.
    Each digit must be sorted in a stable manner in order to maintain the relative ordering of the previously sorted
    digits.

    :param lst: Contains the list to be sorted
    :return: output_list: Return sorted output list (Sorted from from least significant (rightmost column) to most significant (leftmost column) )
    :pre-condition: List must be a list of integers.
    :post-condition: List is sorted one digit at a time, from least significant (rightmost column) to most significant (leftmost column)
    :worst-case time-complexity: O(KN) -  K is the length of the longest element in list and N is the length of the list
    :best-case time-complexity: O(KN)  - K is the length of the longest element in list and N is the length of the list
    """

    output_list = lst

    longestNum = maxDigitVal_2(lst)


    for digit in range(1, longestNum + 1):
        output_list = radix_pass_integers(output_list, 10, digit)
    return output_list




#_______________________________________________________________________________________________________________________

# Task 2




def remove_duplicates_v2(duplicate):
    """
    This function aims to remove duplicate tuples from a list called - "duplicate".
    This function outputs a list containing unique tuples.
    However, the output list may contain tuples that have one element of the tuple in common, but the other element being different.
    This is fine because each tuple is still unique, despite some tuples having one element in common.

    :param duplicate: List containing duplicate tuples,
    :return: final_list: A list of unique tuples.
    :pre-condition: Input Must be  a list.
    :post-condition: Returns a list of unique elements.
    :worst-case time-complexity: O(N) - where N is length of list containing duplicates
    :best-case time-complexity: O(N) -  where N is length of list containing duplicates

    :param duplicate:
    :return:
    """
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list


def check_duplicates_v2(word, sublist):
    """
    This function checks for the presence of a "word" in a sublist by iterating through the first elements of a list of tuples
    in "sublist" and if a match is found for word, the second element of that tuple is added to a "id_list"
    The function then returns the id_list which contains a list of corresponding Song ID's of Songs which contain the word being searched.

    :param word: The word being searched for which corresponding ID's are found for.
    :param sublist: The list of tuples, the first element (0th index) of the tuples is iterated through to find a match for the word
    :return: id_list: List of ID's of Songs which contain the "word"
    :pre-condition: Each element of the list must be a tuple and first element of tuple contains word
    :post-condition: Return list of ID's of Songs which contain the "word"
    :worst-case time-complexity:O(N) Where N is the length of sublist
    :best-case time-complexity:O(N) Where N is the length of sublist

    """
    id_list = []
    for i in range (len(sublist)):
        if sublist[i][0] == word:
            id_list.append(sublist[i][1])
    return id_list




def collate(filename):

    """
    The function takes as input a string of a "filename"
    The function will collect the song IDs of each word, and output the unique words together with their song IDs
    to another file.
    collate will write output to a file named "collated_ids.txt" (which it will create).
    This file will consist of U lines, where U is the number of unique words in the input file.
    Each line will start with a word, then a colon, and then all the song IDs of the songs which contain that word
    (separated by spaces). The song IDs in each line will appear in ascending order.
    The order of the lines depends on the words. If the word in line x is lexicographically less than the word in
    line y, then x will appear before y in collated_ids.txt.


    Algorithm Walk-through:

    The function starts off by reading in the lines of file into a list of "tuples" of word-ID pairs.
    I then removed all the duplicate tuples from the list using function remove_duplicates,
    and the remaining list of unique tuples will contain occurrences whereby certain unique tuples may have the
    first element of the tuple - (word) in common but different song ID.
    We then iterate over the list of unique tuples and for each tuple looked at we run a function check_duplicates_v2
    which takes as input the first element of the tuple (word) and the list of unique tuples.
    The function check_duplicates_v2 then returns all the ID's associated to that word. and appends the word and list of
    associated ID's into a list "final_list" .
    Note at this point final_list contains a list of tuples where the first element of each tuple is the word and the second
    element of the tuples is a list of associated song ID's.
    However final_list will contain duplicate tuples, because initially when building this final_list we took as input a list of uniqe tuples
    but there were instances where certain tuples contained the same word but differnt song ID's.
    We solve this problem by running the function remove_duplicates a second time, giving as input the "final_list".
    After running remove_duplicates we have a new list - (name: "final_sorted") of unique tuples, each tuple containing a word as its first element and
    a list of associated song ID's as its second element.

    We then open a new file collated_ids.txt and
    then iterate over the "final_sorted" list and for each tuple in the list, we iterate over the list of ID's,
    for each word (first element of tuple) we write to the file the word and the corresponding IDs.
    This repeates for each ID in the list.
    THe file is then closed.




    :param filename: the name of file containing the word and corresponding song ID (one in each line)
    :return: writes a file containing a word and all the assoicates IDs in each line
    :worst-case time-complexity:O(TM) T is the total number of words over all songs in the input file, M is the length of the longest word
    :best-case time-complexity:O(TM) T is the total number of words over all songs in the input file, M is the length of the longest word

    """

    file = open(filename, 'r')
    tuples = []

    for line in file:

        index_colon = line.index(':')

        word = line[0:index_colon]
        id = line[index_colon + 1:]

        new_line = id.split()

        for id_select in new_line:
            tuples.append([word, id_select])
        # print(tuples)
    file.close()


    list_no_duplicates = remove_duplicates_v2(tuples)
    final_list = []

    for i in range(len(list_no_duplicates)):
        id_list = check_duplicates_v2(list_no_duplicates[i][0], list_no_duplicates)
        final_list.append((list_no_duplicates[i][0], id_list))

    final_sorted = remove_duplicates_v2(final_list)

    #return final_sorted




    file = open("collated_ids.txt", 'w')
    for i in range(len(final_sorted)):
        ids=final_sorted[i][1]
        ids_string=" "
        for id in ids:
            ids_string+= str(id) + "  "
        file.write(final_sorted[i][0] + ':' + ids_string + '\n')
    file.close()



#_______________________________________________________________________________________________________________________

# Task 3

def lookup(collated_ids, query):
    """
    which takes as input two filenames, and for each word in query_file determines the songs which contain that word.
    The input to this task consists of two files. The first, collated_file, will be the same format as a file produced
    by the collate function from task 2. The second file, query_file contains words, each one on a separate line.

    lookup will write output to a file named "song_ids.txt".
    This file will contain the same number of lines as query_file. If the word on line i of query_file appears in at
    least one song, then line i of "song_ids.txt" will contain the song IDs (in ascending order, separated by spaces)
    that contain that word. If the word does not appear in any song, then the corresponding output line should
    be the string "Not found".

    Algorithm Walk-through:

    The function starts off by reading in the lines of "collated_ids" file into a list of 'tuples' of word-ID_List pairs.
    The function then proceeds to read the word in each line of "query" file into list 'query_array'.
    I then iterate over the length of the query_array and for each word in query array we do a binary search ( time complexity - log(N))
    by giving as input the word and the list of 'tuples'.

    This binary search returns the 'index' of that word in the list of 'tuples' and we fetch the list of ID's by accessing the second element of
    the tuples at the 'index'. These ID's are the appended to a list called 'ids'.

    If the binary seach returns 'None' we append the string "Not Found". This string is then appended to  the 'ids' list

    We then open a new file "song_ids.txt".
    and then iterate over the length of 'ids' array and for each element in 'ids' we write into a new line in the file "song_ids.txt"
    The file 'song_ids' is then closed.


    :param collated_ids: The file to read the list of sorted words and corresponding ID's
    :param query: The file containing the words (one in each line) for which we search each word in collated_ids
    :return: writes a file containing the ID's corresponding to each of the words given in query file.
    :worst-case time-complexity: O(q × Mlog(U) + P)
    :best-case time-complexity: O(q × Mlog(U) + P),

    Note: q is the number of words in query_file, M is the length of the longest word in any song,
    U is the number of lines in collated_file, P is the total number of IDs in the output

    """

    file = open(collated_ids, 'r')
    tuples = []

    for line in file:

        index_colon = line.index(':')

        word = line[0:index_colon]
        id = line[index_colon + 1:]

        id_array = id.strip()

        tuples.append((word, id_array))
    file.close()

    file2 = open(query, 'r')
    query_array = file2.read().splitlines()
    file2.close()


    ids = []
    for i in range(len(query_array)):
        index = binarySearch(query_array[i], tuples)

        if index != None:
            ids.append(str(tuples[index][1]))
        else:
            ids.append("Not Found")


    file = open("song_ids.txt", 'w')

    for i in range(len(ids)):
        file.write(ids[i] + '\n')
    file.close()



def binarySearch (word, sequence):
    """
    The function Binary Search returns the index of the 'word' being searched for in list of tuples - 'sequence'

    :param word: The word whose index we are seeking.
    :param sequence: The array of tuples which we are searching for 'word'
    :return: index of the word in list of tuples, or return 'None' if the word is not present in the array
    """
    lower_bound = 0
    upper_bound = len(sequence) -1
    while lower_bound<=upper_bound:
        mid = (lower_bound+upper_bound)// 2
        if sequence[mid][0] == word:
            return mid
        elif sequence[mid][0] > word:
            upper_bound = mid -1
        else:
            lower_bound = mid+1
    return None



#_____________________________________________________________________________________________________________________#





if __name__ == "__main__":
    process("example_songs.txt")
    collate("sorted_words.txt")
    lookup("collated_ids.txt", "example_queries.txt")