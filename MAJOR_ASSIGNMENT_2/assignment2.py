

# Task 1

def best_score(pile1,pile2):
    """
    The purpose of this function is to determine optimal play for the coin taking game.
    It will determine the highest score which can be achieved by player 1, assuming that both players play optimally.

    The function takes as input Two lists, pile1 and pile2.
    These lists contain integers which represent the values of the coins in the game.
    The numbers in pile1 are the values of coins in the first pile, where pile1[i] is the value of the coin with i coins
    beneath it in the pile. pile2 represents the coins in the second pile in the same way.
    The function handles when piles may be empty.

    Tne function returns a A tuple with two elements.
    The first is a single number which represents the highest score which player 1 can achieve.
    The second represents the choices made by both players during the game (assuming optimal play).

    The choices are represented by a list containing only the numbers 1 and 2, where a 1 indicates that the player
    took the top coin from pile1 on their turn, and 2 indicates that the player took the top coin from pile2 on their turn.

    :param pile1: The first pile of coins
    :param pile2: The second pile of coins
    :return: a Tuple, first element of tuple is the highest score that player1 can achieve, the second element is the
             choices made by both players during the game (assuming optimal play).
    """

    if len(pile1)==0 and len(pile2) == 0:   # accounting for scenario where both piles are empty.
        return [0,[]]

    elif len(pile1)==0:     # Accounting for senario where one pile1 is empty.
        memo = [0 for i in range(len(pile2)+1)]
        memo[1] = pile2[0]
        for i in range(2, len(pile2) + 1):
            memo[i] = memo[i - 2] + pile2[i - 1]    # Memoize the total score of the players at each turn


        if (len(pile2) % 2) == 1:   # If there are odd number of coins in the pile,
                                # The last element of the memo contains the max value that can be obtained by player1
            return [memo[len(memo)-1],backtrack_one_dimen(memo,2)]
        else:
            return [memo[len(memo)-2], backtrack_one_dimen(memo,2)]     # If there is a even number of coins in the pile,
                                # The before-last element of memeo contains max-value that can be obtained by player1



    elif len(pile2)==0:      # Accounting for senario where one pile2 is empty.
        memo = [0 for i in range(len(pile1)+1)]
        memo[1] = pile1[0]
        for i in range(2, len(pile1) + 1):
            memo[i] = memo[i - 2] + pile1[i - 1]        # Memoize the total score of the players at each turn

        if (len(pile1) % 2) == 1: # If there are odd number of coins in the pile,
                                # The last element of the memo contains the max value that can be obtained by player1
            return [memo[len(memo)-1],backtrack_one_dimen(memo,1)]
        else:
            return [memo[len(memo)-2], backtrack_one_dimen(memo,1)] # If there is a even number of coins in the pile,
                                # The before-last element of memeo contains max-value that can be obtained by player1


    elif len(pile1) >0 and len(pile2) >0 :  # Accounting for hen both piles have more than one coin

        memo = [[0 for i in range(len(pile1) + 1)] for i in range(len(pile2) + 1)]

        totals_pile1 = sum_pile(pile1)
        totals_pile2 = sum_pile(pile2)

        memo[0][0] = 0      # Assigning first element of 2D array to be 0, thus accounting for the null set.
        memo[0][1] = pile1[0]   # The second element of first row [index 0] will be first element of pile1

        for i in range(2, len(pile1) + 1):      # Filling the first row with the optimal values given both players pick from pile1
            memo[0][i] = memo[0][i - 2] + pile1[i - 1]
        # print(memo)

        memo[1][0] = pile2[0]   # The first element of the second row will be the first element of pile2
        for j in range(2, len(pile2) + 1):  # Filling the first collumn of each row (after first row, because row1,col1 contains 0) with the optimal values given both players they from pile2
            memo[j][0] = memo[j - 2][0] + pile2[j - 1]
        # print(memo)

        # Filling the elements in the 2D memo, from row[1] to row[n-1] and col[1] to col[n-1]
        # Any element that is outside the first row and first column of the memo, (but whithin the bounds of the memo)
        # is filled by finding the sum of both piles upto that respective index and substracting the next miniimum adjacent element (minimum adjacent optimum value).
        # This represents the optimal value of that given combination of elements in pile1 and pile2

        for j in range(1, len(pile2) + 1):
            for i in range(1, len(pile1) + 1):
                memo[j][i] = totals_pile1[i - 1] + totals_pile2[j - 1] - min(memo[j][i - 1], memo[j - 1][i])
        #print(memo)
        # print("\n")
        # for row in memo:
        #     print(row)

        optimum = memo[len(memo) - 1][len(memo[len(memo) - 1]) - 1]
        # The optimum value for Player 1 is always the last index of the memo, based on the fact that player 1 goes first

        return [optimum, backtrack(memo)]





def sum_pile(pile):
    """
    This function returns a list containing the sum of the elements of the pile at each index of the pile.
    This is meant to emulate the the sum of coins after each removal of each coin, until the last coin is removed

    :param pile: The pile being iterated over
    :return: A list containing the sum of elements of the pile at each index of the pile, untill the end of pile.
    :Best Case Time-Complexity: O(n)
    :Worst Case Time-Complexity: O(n)
    """
    totals_pile = [0 for i in range(len(pile))]
    for i in range(len(totals_pile)):
        if (i == 0):
            totals_pile[0] = pile[0]
        else:
            totals_pile[i] = totals_pile[i - 1] + pile[i]
    return totals_pile


def backtrack(memo):
    """
    This function returns the list containing the series of choices made by both players, both operating optimally.
    This is done by a process known as backtracking where we initialize the pointer, j_index (ROW) as the last row
    and the i_index (column) as the last column of the last row.

    We then proceed to check the 2 adjacent elements above (top) and to the left.
    If the element to the left is less than the element above,  we move the pointer to the left.
    If the element above is less than the element to the left, we move the pointer above.
    If in the circumstance where both the top element and element to the left are equal, move the pointer up.

    We move the pointer based on nearest adjacent elements because both players when operating optimally will aim to reduce the total of the oponent

    Which is why when building the memo, we considered the total sum of the coins(removed) in the pile at each point and subtract
    the minimum adjacent element.
    The logic being that we find the sum of coins of both piles at each point (of both piles in memo) and then subtract the least total coins (to be given to oponent)
    because each player thinking optimally will aim to minimize the total of the opponent
    leaving the player with the sum of piles - min(adjacent total ), which is the maxiimum the player can have at that point.

    Therefore we keep moving the pointer in this manner until the pointer reaches the first element
    of the memo (memo[0][0]) at which point the list of decisions is returned.

    In this manner we are able to determine the optimal choices made by both players.


    :param memo: The memo being traversed through
    :return: list containing the series of choices made by both players, both operating optimally.
    Time-Complexity: O(n+m) ; where n is the number of elements in pile 1 and m is the number of elements in pile 2
    """

    # print("\n")
    # print(memo)
    j_index = len(memo) - 1
    i_index = len(memo[len(memo) - 1]) - 1

    backtrack_path = []

    Done = False
    while not Done:
        if j_index == 0 and i_index == 0:       # If pointer is at the fist element of the memo, (Memo[0][0]), set Done to True and stop the loop
            Done = True
        elif j_index == 0 and memo[j_index][i_index-1] < memo[j_index][i_index]: # if the pointer is at the first row, keep moving pointer left, appending 1 to the back_tarck path
            if i_index == 0 and j_index == 0:
                break
            i_index = i_index - 1    # Move pointer left
            backtrack_path.append(1)    # append 1 to indicate choice from first pile
        elif memo[j_index][i_index - 1] < memo[j_index - 1][i_index]:   # if the element to the left is less than element on top, move pointer left
            if i_index == 0 and j_index == 0:
                break
            i_index = i_index - 1   # Move pointer left
            backtrack_path.append(1)    # append 1 to indicate choice from first pile
        elif memo[j_index - 1][i_index] < memo[j_index][i_index - 1]:   # If the element on top is less that the element on the left, move pointer up
            if i_index == 0 and j_index == 0:
                break
            j_index = j_index - 1   # Move pointer up
            backtrack_path.append(2)    # append 2 to indicate choice from second pile
        elif memo[j_index - 1][i_index] == memo[j_index][i_index - 1]:  # If element to left and element on to is the same, move pointer up.
            if i_index == 0 and j_index == 0:
                break
            j_index = j_index - 1   # Move pointer up
            backtrack_path.append(2)    # append 2 to indicate choice from second pile
    return backtrack_path


def backtrack_one_dimen(memo,append_val):
    """
    This function is used to backtrack a 1D memo created if one of the piles is empty
    :param memo: The array to traverse
    :param append_val: The value to append to the backtrack path. varies based on which pile is empty.
    :return: list containing the series of choices made by both players, both operating optimally.
    Time-Complexity: O(n) ; where n is the number of elements being backtracked through.
    """
    i_index = len(memo)-1

    backtrack_path = []

    for i in range(len(memo),1,-1):
            backtrack_path.append(append_val)
    return backtrack_path





#______________________________________________________________________________________________________________________

#Task 2



def is_in(grid, word):
    """
    This function is find a word in a given Snake-words grid
    Input given: grid is a list of length N, each element of which is a list of length N.
    The elements of the internal lists are all single lowercase english alphabet characters (a-z).
    grid[i][j] represents the letter in the ith row and jth column of grid.

    If grid does not contain word then is_in returns False.
    If grid does contain word, is_in returns a list of tuples, which represent the grid cells that correspond to the word.

    :param grid: The grid of alphabetical letters being checked for a word in sequence.
    :param word: The word being searched for
    :return:  If grid does not contain word then returns False.
              If grid does contain word, returns a list of tuples, which represent the grid cells that correspond to the word.
    """
    assert(len(grid) == len(grid[0]))   # Asserting that the grid is N x N

    if len(word) == 0:  # If the word is empty, return false.
        return False

    if len(grid) == 0:  # If the grid is empty, return false.
        return False

    memo = []       # Initiate a empty array for memoization
    for i in range(len(word)):  # Iterate over the length of the word, and for each element in the word, append an empty array to the memo
        row = []
        memo.append(row)
    #print(memo)

    # Iterate over the elements of the grid in search of the first character of the word, if found append the coordinates
    # of that element in a tuple, enclosed in a list, to the first list in memo
    for row in range(len(grid)):
        for col in range(len(grid)):
            if word[0] == grid[row][col]:
               memo[0].append([(row,col)])
    #print(memo)



    for i in range(1,len(memo)):       # Iterating over the memo from second element in memo (a list) to last element
        sth = []
        for k in range(len(memo[i - 1])):   # Iterating over the contents of the memo[i-1] list, where the lists of memo contain the coordinates of the substrings.
            # print(f"tuple is {memo[i - 1][k][-1]}")
            #print(f"tuple is {memo[i - 1][k]}")
            row = memo[i - 1][k][-1][0]     # Accessing the last tuple of the memo[i-1][k] list and assigning the first element of tuple to row
            col = memo[i - 1][k][-1][1]     # Accessing the last tuple of the memo[i-1][k] list and assigning the second element of tuple to col

            index_list = check_adj_positions(grid, word[i], row, col)   # a list of coordinates of the charatcer being seeked (word[i] which is the next element of word).
                                                                        # The coordinates are those which are adjacent to the start position (row, col)
            if len(index_list) > 0: # If len(index_list) is greater than 0, the next charaacter of word substring can be found in the grid adjacent to the position of the previous character (in grid )
                o_index = memo[i - 1][k]    # List containing the coordinates of tuples of word characters found in sequence, forming a substring of thr word
                for item in index_list:
                    sth += [o_index+[item]]
                #print(sth)
                memo[i] =sth        # The element of Memo is assigned to be the list containing the coordinates of tuples of word characters (forming a substring) found in sequence (Word Substring)
            else:
                continue
        #print(memo)
    #print(memo[-1][0])
    if len(memo[-1]) > 0:   # The last element in memo contains, if any, lists with the coordinates of tuples of all word characters found in sequence. This is a path to the given word.
        if len(memo[-1][0]) == len(word): # If the length of list contained in the last element of memo (as described above) is equal to the lenght of word.
            return memo[-1][0]  # Return the list
        else:
            return False    # Else return false
    else:
        return False    # if length of last element of Memo < 0, return false.



def check_adj_positions(grid,seek_char,start_row,start_collumn):
    """
    This function is used to find the possible adjacent coordinates of the character (seek_char) being seeked, from the start position
    grid[start_row, start_collumn], IF the character is adjacent to the initial coordinate (start_rpwq, start_collumn)
    When looking for the possible adjacent coordinates of the character being seeked in the grid, from the initial index,
    there are at MOST 8 possible directions (up, down, left, right, right-up-diagonal,left-up-diagonal,right-down-diagonal, left-down-diagonal)
    There are also several other possible directions possible based on the initial position of the start_row, start_collumn.

    All possiblities are accounted for.


    :param grid: The grid being traversed over, checking all possible adjacent positions for the seek_char from start_row and start_collumn
    :param seek_char: The character being seeked for in the grid from starting position,
    :param start_row: Start position row
    :param start_collumn: Start position collumm
    :return: a list of coordinates if the charatcer being seeked. The coordinates are those which are adjacent to the start position (start_row, start_collumn)
    """
    row = start_row
    col = start_collumn

    index_list = []
    # print("\n start row and collumn is ")
    # print(start_row,start_collumn)
    if start_row == 0:      # If start position (start_row) is in first row

        if start_collumn == 0:     # If start position (start_col) is in first col
            # Checking if seek_char present in the 3 possible directions

            if grid[row][col+1] == seek_char:
                index_list.append((row,col+1))

            if grid[row+1][col]==seek_char:
                index_list.append((row+1,col))

            if grid[row+1][col+1]==seek_char:
                index_list.append((row+1,col+1))

        elif start_collumn == len(grid[1])-1:   # If start position (start_col) is in last col
            # Checking if seek_char present in the 3 possible directions

            if grid[row][col - 1] == seek_char:
                index_list.append((row, col - 1))

            if grid[row + 1][col] == seek_char:
                index_list.append((row + 1, col))

            if grid[row + 1][col - 1] == seek_char:
                index_list.append((row + 1, col - 1))

        elif start_collumn >0 and start_collumn < len(grid[1])-1:   # If start position (start_col) is in between first and last col
            # Checking if seek_char present in the 5 possible directions

            if grid[row][col - 1] == seek_char:
                index_list.append((row, col - 1))

            if grid[row][col+1] == seek_char:
                index_list.append((row,col+1))

            if grid[row+1][col]==seek_char:
                index_list.append((row+1,col))

            if grid[row + 1][col - 1] == seek_char:
                index_list.append((row + 1, col - 1))

            if grid[row+1][col+1]==seek_char:
                index_list.append((row+1,col+1))

    elif start_row == len(grid)-1:  # If start position (start_row) is in last row

        if start_collumn == 0:  # If start position (start_col) is in first col
            # Checking if seek_char present in the 3 possible directions

            if grid[row][col+1] == seek_char:
                index_list.append((row,col+1))

            if grid[row-1][col]==seek_char:
                index_list.append((row-1,col))

            if grid[row-1][col+1]==seek_char:
                index_list.append((row-1,col+1))

        elif start_collumn == len(grid[1])-1:# If start position (start_col) is in last col
            # Checking if seek_char present in the 3 possible directions

            if grid[row][col - 1] == seek_char:
                index_list.append((row, col - 1))

            if grid[row - 1][col] == seek_char:
                index_list.append((row - 1, col))

            if grid[row - 1][col - 1] == seek_char:
                index_list.append((row - 1, col - 1))

        elif start_collumn > 0 and start_collumn < len(grid[1]) - 1:    # If start position (start_col) is in between first and last col
            # Checking if seek_char present in the 5 possible directions

            if grid[row][col - 1] == seek_char:
                index_list.append((row, col - 1))

            if grid[row][col + 1] == seek_char:
                index_list.append((row, col + 1))

            if grid[row - 1][col] == seek_char:
                index_list.append((row - 1, col))

            if grid[row - 1][col - 1] == seek_char:
                index_list.append((row - 1, col - 1))

            if grid[row - 1][col + 1] == seek_char:
                index_list.append((row - 1, col + 1))
    elif start_row > 0 and start_row <len(grid)-1:# If start position (start_row) is in between first and last row

        if start_collumn == 0:  # If start position (start_col) is in first col
            # Checking if seek_char present in the 5 possible directions

            if grid[row][col+1] == seek_char:
                index_list.append((row,col+1))

            if grid[row-1][col]==seek_char:
                index_list.append((row-1,col))

            if grid[row+1][col]==seek_char:
                index_list.append((row+1,col))

            if grid[row-1][col+1]==seek_char:
                index_list.append((row-1,col+1))

            if grid[row+1][col+1]==seek_char:
                index_list.append((row+1,col+1))

        elif start_collumn == len(grid[1])-1:    # If start position (start_col) is in last col
            # Checking if seek_char present in the 5 possible directions

            if grid[row][col - 1] == seek_char:
                index_list.append((row, col - 1))

            if grid[row - 1][col] == seek_char:
                index_list.append((row - 1, col))

            if grid[row + 1][col] == seek_char:
                index_list.append((row + 1, col))

            if grid[row - 1][col - 1] == seek_char:
                index_list.append((row - 1, col - 1))

            if grid[row + 1][col - 1] == seek_char:
                index_list.append((row + 1, col - 1))

        elif start_collumn > 0 and start_collumn < len(grid[1]) - 1:    # If start position (start_col) is in between first and last col
            # Checking if seek_char present in the 8 possible directions

            if grid[row][col - 1] == seek_char:
                index_list.append((row, col - 1))

            if grid[row][col + 1] == seek_char:
                index_list.append((row, col + 1))

            if grid[row - 1][col] == seek_char:
                index_list.append((row - 1, col))

            if grid[row + 1][col] == seek_char:
                index_list.append((row + 1, col))

            if grid[row - 1][col - 1] == seek_char:
                index_list.append((row - 1, col - 1))

            if grid[row + 1][col - 1] == seek_char:
                index_list.append((row + 1, col - 1))

            if grid[row - 1][col + 1] == seek_char:
                index_list.append((row - 1, col + 1))

            if grid[row + 1][col + 1] == seek_char:
                index_list.append((row + 1, col + 1))
    return index_list





if __name__ == "__main__":

    print(f"Task 1: \nFor Given Test Case: [5,8,2,4,1,10,2],[6,2,4,5,6,9,8] \n{best_score([5,8,2,4,1,10,2],[6,2,4,5,6,9,8])} \n\n")

    grid = [['a','b','c','d'], ['e','a','p','f'], ['e','p','g','h'], ['l','i','j','k']]
    word1 ='apple'
    print(f"Task 2: \nFor given Test Case: \nGrid: {grid} , \nWord: {word1} \n{is_in(grid,word1)} ")






