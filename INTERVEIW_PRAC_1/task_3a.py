'''
Name: Hewa Annakkage Gaveen Senal Lakpura Amarapala
Student ID: 29491479
'''


def bubble_sort(the_list):
    n = len(the_list)
    n = n-1

    for i in range(len(the_list)-1):        #Loop Repeats for n-1 iterations

        for j in range(n):

            # Traverse the list (0 - n)
            # Swap if the element > next element
            if the_list[j] > the_list[j+1]:  #if initial value is greater than adjacent value, the two values are swapped
                temp = the_list[j+1]
                the_list[j+1] = the_list[j]
                the_list[j] = temp

    return the_list


def testingBubbleSort():
    size = int(input("Enter list size: "))
    the_list = [0] * size

    for i in range(size):
        the_list[i] = int(input("Enter element " + str(i) + " :"))

    sortedList = bubble_sort(the_list)
    print("The Sorted List : " + str(sortedList))


testingBubbleSort()

#bubble_sort([5,7,-9,1,-3,0,1,2,3,11,88])
#bubble_sort([-14,-55,1,7,44,33,8,76,54,32,1,4,3,6,2,-9,-7,5,6,12])

