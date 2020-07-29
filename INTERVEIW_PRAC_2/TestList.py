#!/usr/bin/python3
from ListADT import ListADT

def test_len():
    """function tests length of list"""
    x = ListADT()
    # check if length of initial list is 0.
    assert len(x) == 0, "Length should be 0 but is " + str(len(x))
    x.insert(0, 2)
    # checks length of list = 1 after insertion
    assert len(x) == 1, "Length should be 1 but is " + str(len(x))
    x.unsafe_set_array([1,2,3,3,4,5,5,6,7,6,8,None,None],11)
    # checks if length of list = 11
    assert len(x) == 11,"Length should be 11 but is" + str(len(x))

def test_str():
    """function test string representation of list"""
    x = ListADT()
    # checks if empty string returned for empty ListADT
    assert str(x) == "", "Should be empty string but it is" + str(x)
    x.insert(0, 2)
    # checks if 2 returned
    assert str(x) == "2\n", "Should be a 2 string but it is" + str(x)
    x.unsafe_set_array([1, 2, 3, None, None], 3)
    # Check string containing 1,2,3 returned
    assert str(x) == "1\n2\n3\n", "Should be a 1 2 3 string but it is" + str(x)

def test_contains():
    """function checks whether list contains an element"""
    x = ListADT()
    # checks if 2 in a empty listADT
    assert (2 in x) == False, "Should be False as x is empty but it is" + str(x)
    x.insert(0, 2)
    # check if numeber 2 present within list containing 2 at index 0
    assert (2 in x), "Should be True as x=[2] but it is" + str(x)
    x.unsafe_set_array([4, 2, 3, None, None], 3)
    # checks if 3 is in list that has 3 as a element
    assert (3 in x), "Should be True as x=[4,2,3] but it is" + str(x)

def test_getitem():
    """function gets element from a specific index"""
    x = ListADT()
    x.unsafe_set_array([4,3,5,6, None, None], 4)
    # if 4 is in position 0
    assert (x[0] == 4), "Should be 4 but it is" + str(x[0])
    # if 3 is in position 1
    assert (x[1]== 3), "Should be 3 but it is" + str(x[1])
    # if 6 is in position 3
    assert (x[3] == 6), "Should be 6 but it is" + str(x[3])
    try:
        # checks if IndexError raised when index is out of range
        x[7] == 0
        print("Should have raised IndexError")
    except IndexError:
        True

def test_setitem():
    """function sets element in a specific position"""
    x = ListADT()
    x.unsafe_set_array([4,3,5, None, None], 3)
    # if value at index 0 is changed to 10
    x[0]=10
    # if value at  1 is changed to 20
    x[1]=20
    # if value at  2 is changed to 30
    x[2]=30
    assert (x[0] == 10), "Should be 10 but it is" + str(x[0])
    assert (x[1] == 20), "Should be 20 but it is" + str(x[1])
    assert (x[2] == 30), "Should be 30 but it is" + str(x[2])
    try:
        # checks if IndexError raised when index is out of range
        x[7] = 0
        print("Should have raised IndexError")
    except IndexError:
        True

def test_eq():
    """function checks whether two lists are equal"""
    x = ListADT()
    x.unsafe_set_array([4, 3, 5, None, None], 3)
    y = ListADT()
    y.unsafe_set_array([4, 3, 5, None, None], 3)
    z = ListADT()
    z.unsafe_set_array([4, 5, 3, None, None], 3)
    w = ListADT()
    w.unsafe_set_array([4, 5, None, None], 2)
    # tests if two lists with same elements are equal
    assert (x==y), "Should be True but it is" + "x="+ str(x) + "y=" + str(y)
    # tests if two lists with different element are not equal
    assert (x != z), "Should be False but it is" + "x="+ str(x) + "z=" + str(z)
    # tests if two lists with different element are not equal
    assert (x != w), "Should be False but it is" + "x="+ str(x) + "w=" + str(w)
    try:
        # checks if IndexError raised when index is out of range
        x[7] = 0
        print("Should have raised IndexError")
    except IndexError:
        True

def test_insert():
    """function checks whether an element is inserted correctly"""
    x = ListADT()
    x.unsafe_set_array([1, 2, 5, 6, 7, None, None], 5)
    y = ListADT()
    y.unsafe_set_array([1, 2, 3, 5, 6, 7,  None], 6)
    x.insert(2, 3)
    # check if x and y are equal, after inserting 3 in position 2
    assert (x == y), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)
    x.insert(0, 0)
    y.unsafe_set_array([0, 1, 2, 3, 5, 6, 7, None], 7)
    # check if x and y are equal, after inserting 0 in position 0
    assert (x == y), "Should be True but it is" + "x=" + str(x) + "y=" + str(y)
    # tests if inserting to a list which is full is raising IndexError
    try:
        x.insert(12,2)
        print("Should have raised IndexError")
    except IndexError:
        try:
            x.insert(1, 2)
            print("Should have raised Exception")
        except Exception:
            True

def test_delete():
    """function tests whether element at index is deleted"""

    x = ListADT()
    x.unsafe_set_array([1, 2, 5, 6, 7, None, None], 5)
    y = ListADT()
    y.unsafe_set_array([1, 2, 6, 7, None, None], 4)
    item = x.delete(2)
    # checks if functions deletes 5 from position 2, and if  item equals 5
    assert (item == 5 and x == y), "Should be True but it is" + "item=" +str(item)+"x=" + str(x) + "y=" + str(y)
    item = x.delete(0)
    y.unsafe_set_array([2, 6, 7, None, None], 3)
    # checks if functions deletes 1 from position 0 and if item equals 1
    assert (item == 1 and x == y), "Should be True but it is" + "item=" + str(item) + "x=" + str(x) + "y=" + str(y)
    # tests if deleting from a list at an invalid index is raising IndexError
    try:
        x.delete(12)
        print("Should have raised IndexError")
    except IndexError:
        True

def main():
    # Run the tests when the module is called from the command line
    ListADT.in_test_mode = True
    try:
        print("Testing length")
        test_len()
        print("Testing str")
        test_str()
        print("Testing contains")
        test_contains()
        print("Testing getitem")
        test_getitem()
        print("Testing setitem")
        test_setitem()
        print("Testing eq")
        test_eq()
        print("Testing insert")
        test_insert()
        print("Testing delete")
        test_delete()
    except Exception as e:
        print("Error, unexpected exception: ", e)

if __name__ == '__main__':
    main()
