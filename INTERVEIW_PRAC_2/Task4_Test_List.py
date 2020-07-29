from Task4 import *
from Task2 import ListADT

def testing_insert():



    x = Editor()
    x.text_lines = read_text_file('small.txt')
    list_of_strings = ListADT()
    list_of_strings.insert(0,'lol what is this')
    x.insert_num_strings(4,list_of_strings)

    y = ListADT()
    for i in ['Yossarian decided', 'not to utter','another word.', 'lol what is this']:
        y.append(i)

    # Check if insert function is correctly inserting to correct position by comparing 2 lists./
    # both which should contain the same elements.
    assert (x.text_lines.the_array == y.the_array), "Should be True, but  \nx = " + str(x.text_lines) + "\n y = " + str(y)


    x = Editor()
    x.text_lines = read_text_file('small.txt')
    list_of_strings = ListADT()
    list_of_strings.insert(0,'My Friend')
    x.insert_num_strings(1,list_of_strings)


    y = ListADT()
    for i in ['My Friend','Yossarian decided', 'not to utter','another word.']:
        y.append(i)
    # Check if insert function is correctly inserting to correct position by comparing 2 lists./
    # both which should contain the same elements.
    assert (x.text_lines.the_array == y.the_array), "Should be True, but  \n x = " + str(x.text_lines) + "\n y = " + str(y)




    x = Editor()
    x.text_lines = read_text_file('small.txt')
    list_of_strings = ListADT()
    list_of_strings.insert(0, 'He is a')
    list_of_strings.insert(1, 'Good Friend')
    x.insert_num_strings(-1, list_of_strings)

    y = ListADT()
    for i in ['Yossarian decided', 'not to utter', 'another word.', 'He is a','Good Friend']:
        y.append(i)
    # Check if insert function is correctly inserting to correct position by comparing 2 lists./
    # both which should contain the same elements.
    assert (x.text_lines.the_array == y.the_array), "Should be True, but  \n x = " + str(
        x.text_lines) + "\n y = " + str(y)




def testing_delete():

    x = Editor()
    x.text_lines = read_text_file('small.txt')
    x.delete_num(1)

    y = ListADT()
    for i in ['not to utter','another word.']:
        y.append(i)
    # Check if delete function is correctly deleting item at correct position by comparing 2 lists./
    # both which should contain the same elements.
    assert (x.text_lines.the_array == y.the_array), "Should be True, but  \n x = " + str(x.text_lines) + "\n y = " + str(y)


    x = Editor()
    x.text_lines = read_text_file('small.txt')
    list_of_strings =ListADT()
    list_of_strings.insert(0, 'He is a')
    list_of_strings.insert(1, 'Good Friend')
    x.insert_num_strings(-1, list_of_strings)
    x.delete_num(-2)

    y = ListADT()
    for i in ['Yossarian decided', 'not to utter','another word.','Good Friend']:
        y.append(i)
    # Check if delete function is correctly deleting item at correct position by comparing 2 lists./
    # both which should contain the same elements.
    assert (x.text_lines.the_array == y.the_array), "Should be True, but  \n x = " + str(
        x.text_lines) + "\n y = " + str(y)



    x = Editor()
    x.text_lines = read_text_file('small.txt')
    x.delete_num(-1)

    y = ListADT()
    for i in ['Yossarian decided', 'not to utter']:
        y.append(i)
    # Check if delete function is correctly deleting item at correct position by comparing 2 lists./
    # both which should contain the same elements.
    assert (x.text_lines.the_array == y.the_array), "Should be True, but  \n x = " + str(x.text_lines) + "\n y = " + str(y)






def main():
    # Run the tests when the module is called from the command line
    ListADT.in_test_mode = True
    try:
        print("Testing Insert")
        testing_insert()
        print("All's Good!")

        print("Testing Delete")
        testing_delete()
        print("All's Good!")
    except Exception as e:
        print("Error, unexpected exception: ", e)



if __name__ == '__main__':
    main()