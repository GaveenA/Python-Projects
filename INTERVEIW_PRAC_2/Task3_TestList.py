from Task3 import read_text_file
from Task2 import ListADT

def test_read_test_file():
    list_strings = read_text_file('small.txt')
    #checks if the 2nd element of the list is valid
    assert list_strings[2] == 'another word.', "Should be True but is " + str(list_strings[0])
    # checks if the 1st element of the list is valid
    assert list_strings[0]== 'Yossarian decided', "Should be True but is " + str(list_strings[-1])


def main():
    # Run the tests when the module is called from the command line
    ListADT.in_test_mode = True
    try:
        print("Testing Read File ")
        test_read_test_file()
        print("All's Good!")

    except Exception as e:
        print("Error, unexpected exception: ", e)

if __name__ == '__main__':
    main()