from Task6_ListADT import ListADT

def read_text_file(name):
    """
    This Function takes the name of a text file as input and reads each line of text into a string,
    returning a list of strings associated to the file
    (i.e., the function converts the text in the file into a list of strings).
    The function makes use of the List ADT implemented in Task 2 for this, that is,
    the list of strings returned by the function is an object of the ListADT class implemented in Task 2.

    @:param name: name of the text file
    @:return the list of strings created from the content of the text file
    """
    try:
        myfile = open(name)
        string_list = ListADT()

        for i in myfile:
            string_list.append(i.rstrip())
        myfile.close()

        return string_list
    except Exception as error:
        print("Unable to access file: ")
        print(error)
        return None

#print(read_text_file('small.txt'))
