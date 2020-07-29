from Task3 import read_text_file
from Task2 import ListADT
from Task5 import Editor

def test_Task5_search():
    x = Editor()
    x.text_lines = read_text_file('small.txt')
    x.search_string('not')






def main():
    # Run the tests when the module is called from the command line
    ListADT.in_test_mode = True
    try:
        print("Testing search_string")
        test_Task5_search()
        print("All's Good !")

    except Exception as e:
        print("Error, unexpected exception: ", e)

if __name__ == '__main__':
    main()