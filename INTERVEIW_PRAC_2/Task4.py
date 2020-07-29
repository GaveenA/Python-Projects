from Task2 import ListADT
from Task3 import read_text_file






class Editor:

    def __init__(self):
        """
        This method is defined such that the user is allowed to provide the size upon creation.
        If they do not provide size, a default value of 10 is set.

        @:param self: the object
        @Post Condition: Creates an array
        @complexity: Best case O(1), Worst case O(1)
                """

        self.text_lines=ListADT()


    def read_filename(self, name):
        self.text_lines = read_text_file(name)
        print(self.text_lines.the_array)
        print(self.text_lines.size)



    def is_number(self, s):

        """
        Function returns True if index is number, otherwise returns False

        @:param self: the object
        @:param s: input to be tested if number
        @:return String containing the items of the list or returns the empty string if the list is empty
        @Pre Condition: None
        @Post Condition: True if index is number, False if not number
        @complexity: Best case O(1), Worst case O(1)
        """
        try:
            int(s)      # checking if input s is a integer
            return True # Return true if integer
        except ValueError:  # ValueError raised if input is not a integer.
            return False        # Return false if not an integer







    def print_num(self,rest_string):

        """
        Function prints line of text at line given by the user.
        And function Prints all lines of text if user inputs empty string.

        @:param self: the object
        @:param rest_string: valid number (integer)
        @Pre Condition: Input should be a valid number
        @Post Condition: Prints line of text at index = rest_string -1
                        or Prints all lines
        @complexity: Best case O(1), Worst case O(1)

        """



        try:
            if self.is_number(rest_string) == True:  # running is_number() on rest_string to check if its a number
                index = int(rest_string)             # index variable assigned to int(rest_string)
                if index == 0:
                    raise IndexError('Invalid Line Number')     # index error raised if line number input by user = 0
                elif int(rest_string) < 0 and int(rest_string) >= -self.text_lines.length:
                    index = self.text_lines.length+int(rest_string)     # Converting negative index to positive
                    print("\n\n"+ self.text_lines[index])           # printing element at index
                else:
                    index = index - 1      # if index positive,  subtract 1 from index, since index numbers start from 0
                    print("\n\n" + self.text_lines[index])     # printing element at index
            elif rest_string == "":                            # check if rest_string is empty string
                length = len(self.text_lines)
                print("\n\n")
                for i in range (length):
                    print(self.text_lines[i])              # if user inputs empty string, printing all elements in List
            else:
                print("??")
                raise IndexError("Index is not a Number ")   # IndexError raised if index is not a number.
        except Exception as error:                          # All Exceptions in Try block are  caught and printed.
            print("??")
            print(error)
            userInput = input("\nEnter Num of line to print (or nothing to print all lines) : ")
            self.print_num(userInput)    # Giving user another chance to enter correct line_number to print



    def delete_num(self,rest_string):
        """
        Function deletes elements at line given by user,
        if the input is empyty it deletes all lines of text.

        @:param self: the object
        @:param rest_string: valid number (integer)
        @Pre Condition: input should be a valid number
        @Post Condition: Deletes the line of text index = rest_string-1
                        Or delets all lines
        @complexity: Best case O(1), Worst case O(n)
        """
        try:
            if self.is_number(rest_string) == True:     # running is_number() on rest_string to check if its a number

                index = int(rest_string)                # index variable assigned to int(rest_string)
                if index == 0:
                    raise IndexError('Invalid Line Number')     # index error raised if line number input by user = 0

                #print("Deleted Element: ")

                if int(rest_string) < 0 and int(rest_string) >= -self.text_lines.length:
                    index = self.text_lines.length + int(rest_string)    # Converting negative index to positive
                    self.text_lines.delete(index)                        # Deleting element at index
                else:
                    if index >= 1:
                        index = index - 1   # if index positive  subtract 1 from index, since index numbers start from 0
                    self.text_lines.delete(index)                        # Deleting element at index
            elif rest_string == "":         # if user inputs empty string, deleting  all elements in List
                while not self.text_lines.is_empty():
                    index = len(self.text_lines) - 1
                    self.text_lines.delete(index)
            else:
                print("??")
                raise IndexError("Index is not a Number ")           # IndexError raised if index is not a number.
        except Exception as error:                          # All Exceptions in Try block are caught and printed.
            print("??")
            print(error)
            userInput = input("\nEnter Num of line to delete (or nothing to delete all lines) : ")
            self.delete_num(userInput)      # Giving user another chance to enter correct line_number to delete



    def insert_num_strings(self, number, list_of_strings):

        """
        Function inserts individual  elements in  list_of_strings from index = number -1 into self.text_lines.
        Insertion continues until user enters "." by itself.


        @:param self: the object
        @:param number: valid number (integer)
        @:param list_of_strings: List with the elements user enters to be inserted.
        @Pre Condition: input should be a valid number
        @Post Condition: Inserts the new element entered by user at index number-1.
        @complexity: Best case O(1), Worst case O(n)

        """

        try:
            if self.is_number(number) == True:      # running is_number() on number to check if its a number
                number=int(number)                   # index variable assigned to int(number)
                if number == 0:
                    raise IndexError('Invalid line number')     # index error raised if line number input by user = 0
                elif int(number) < 0 and int(number) >= -self.text_lines.length:
                    index = self.text_lines.length + int(number) + 1        # Converting negative index to positive
                elif number > 0:
                    index = number - 1    # if index positive  subtract 1 from index, since index numbers start from 0

            else:
                print("?")
                raise IndexError("Index is not a Number")       # IndexError raised if index is not a number.

        except Exception as error:                   # All Exceptions in Try block are caught and printed.
            print("?")
            print(error)

        try:
            for i in range(len(list_of_strings)):
                self.text_lines.insert(index, list_of_strings[i])  # inserting items in list_of_strings
                index += 1                                         # to self.text_lines at position index
        except Exception as e:                       # All Exceptions in Try block are caught and printed.
            print("?")
            print(e)



    def print_menu(self):
        """
        Function prints Menu

        @:param self: the object
        @Pre Condition: None
        @Post Condition:  Prints the menu
        @complexity: Best case O(1), Worst case O(1)
        """

        print("\n\n***************  MENU  ***************")
        print("\n" + "List of Commands:" + "\n" + "read filename\n" +"print num\n" + "delete num\n" + "insert num\n"
              + "quit\n")



    def prompt_user(self):
        """
        Function calls print_menu.
        Function asks user for selected inputs inputs.
        Function quits when thr user types "quit"

        @:param self: the object
        @Pre Condition: User has to type a command, Exception raised if incorrect command typed by user
        @Post Condition: Calls the appropriate function, and updates the list
        @complexity: Best case O(1), Worst case O(n)

        """


        end = False

        while not end:                      # while end = False the outermost loop runs
            try:
                printMenu = False
                if printMenu == False:
                    self.print_menu()           # Call print menu
                                                # Prompt user to type command
                user_input = input("Enter Command: (eg: read small.txt ) :  \n").lower().split(" ")

                if len(user_input) == 2 and user_input[0]== "read":   # if length of user_input == 2 and first
                        self.text_lines=read_text_file(user_input[1])  # element is "read" call read_text_files()
                                                                        # method and store output in self.text_lines


                # if length of user_input <= 2 and first element is "print" then:
                elif len(user_input)<=2 and user_input[0]=="print":
                    if len(user_input) == 1:                          # if length of user_input == 1
                        rest_string = ""
                        self.print_num(rest_string)                     # initiate print all lines
                    else:
                        self.print_num((user_input[1]))     # else print item at line num  = second user input element



                # if length of user_input <= 2 and first element is "delete" then:
                elif len(user_input) <= 2 and user_input[0] == "delete":
                    if len(user_input) == 1:               # if length of user_input == 1
                        rest_string = ""
                        self.delete_num(rest_string)        # initiate delete all lines
                    else:
                        self.delete_num(user_input[1])  # Else delete item at line num = second element of user input


                # if length of user_input == 2 and first element is "insert" then:
                elif len(user_input)==2 and user_input[0]=="insert":

                    try:
                        # running is_number() on second element of user input to check if its a number
                        if self.is_number(user_input[1]) == True:
                            number = int(user_input[1])        # storing line number as type integer
                            if number == 0:                     # if line number = 0
                                raise IndexError('Invalid line number') # index error raised if line number = 0
                            else:
                                # Creating new ListADT instance to store the content user wants to add
                                list_strings = ListADT()
                                end_insert= False       # setting end_insert condition to false
                                print("Enter text: ")

                                # while end inster = False run while loop to prompt user to type lines to enter
                                while not end_insert:
                                    prompt_user = input(" - ").strip()
                            # if full stop typed by user, set end_insert to true and stop prompting user to type lines
                                    if prompt_user == ".":
                                        end_insert = True
                                    else:
                                        list_strings.append(prompt_user)
                                self.insert_num_strings(user_input[1], list_strings) # List_strings inserted to self
                        else:
                            raise IndexError('Enter valid Line number')  # IndexError raised if index is not a number.
                    except Exception as e:                       # All Exceptions in Try block are caught and printed.
                        print("??")
                        print(e)

                elif len(user_input) == 1 and (user_input[0] == "quit"):
                    # Sets 'end' to true when user types Quit, which stops the outermost while loop from running
                    end = True
                else:
                    print("You must enter one of the listed commands")
                    print("Try again ")
                    self.prompt_user()     # If invalid input is entered, allows user to try again.
            except Exception as e:  # All Exceptions in outer most Try block are caught and printed.
                    end=True
                    print(e)
                    print("??")
                    self.prompt_user()


x=Editor()
x.prompt_user()










