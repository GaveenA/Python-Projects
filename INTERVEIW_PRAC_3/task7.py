from task6 import Freq
from task6_HashTable import HashTable


def main():
    """
    This function reads 3 e-books "warAndPeace.txt", "prideAndPrejudice.txt", "frankenstein.txt" into
     an instance of the Freq class, called dictionary.
     We then create another instance of the Freq class called test_file where we read file "taleOfTwoCities" into
     the test_file.

     We create an instance of HashTable foe the rarity score of words in the test_file

     For each word in the test_file, we access the frequency (occupying position 1 in the tuple) and compare
     it against the rarity method in dictionary.
     This rarity score is then added into the rarity_score_test_file.

     We then run a for loop for all key - score pairs in rarity_score_test_file, and based on the score (0, 1, 2, 3)
     we assign into variables common_word, rare_word, uncommon_word, misspelled_word.

     We then calculate the percentages of common_word, rare_word, uncommon_word, misspelled_word.
     This is printed in Quadruple.
     (common_word_percentage, rare_word_percentage, uncommon_word_percentage, misspelled_word_percentage)


    :return: a quadruple containing
    (common_word_percentage, rare_word_percentage, uncommon_word_percentage, misspelled_word_percentage)
    """





    #reads 3 e-books "warAndPeace.txt", "prideAndPrejudice.txt", "frankenstein.txt" into
    #an instance of the Freq class, called dictionary.

    dictionary = Freq() # Creating an instance of the Freq class created in Task 6

    files = ["warAndPeace.txt", "prideAndPrejudice.txt", "frankenstein.txt"]
    for file in files:
        dictionary.add_file(file)

    #We then create another instance of the Freq class called test_file where we read file "taleOfTwoCities" into
    #the test_file.

    test_file = Freq()
    test_file.add_file("taleOfTwoCities.txt")


    # create an instance of HashTable foe the rarity score of words in the test_file
    rarity_score_test_file = HashTable()


    common_word_count = 0
    rare_word_count = 0
    uncommon_word_count = 0
    misspelled_word_count = 0
    total_word_count = 0


    # For each word in the test_file, we access the frequency (occupying position 1 in the tuple) and compare
    # it against the rarity method in dictionary.
    # This rarity score is then added into the rarity_score_test_file.

    for tuple in test_file.hash_table.array:

        if tuple is not None:
            key = tuple[0]
            frequency = tuple[1]

            rarity_score_test_file[key] = dictionary.rarity(key)
            total_word_count += frequency

    # We then run a for loop for all key - score pairs in rarity_score_test_file, and based on the score (0, 1, 2, 3)
    # we assign into variables common_word, rare_word, uncommon_word, misspelled_word.
    for key_score_pair in rarity_score_test_file.array:
        if key_score_pair is not None:
            key = key_score_pair[0]
            score = key_score_pair[1]

            if score == 0:
                common_word_count += test_file.hash_table[key]

            elif score == 1:
                rare_word_count += test_file.hash_table[key]

            elif score == 2:
                uncommon_word_count += test_file.hash_table[key]

            else:  #score == 3
                misspelled_word_count += test_file.hash_table[key]


    #We then calculate the percentages of common_word, rare_word, uncommon_word, misspelled_word.
     #This is printed in Quadruple.

    common_word_percentage = round((100*common_word_count/total_word_count), 3)
    rare_word_percentage = round((100 * rare_word_count / total_word_count), 3)
    uncommon_word_percentage = round((100 * uncommon_word_count / total_word_count), 3)
    misspelled_word_percentage = round((100 * misspelled_word_count / total_word_count), 3)

    return (common_word_percentage, rare_word_percentage, uncommon_word_percentage, misspelled_word_percentage)




if __name__ == '__main__':
  output_percentages = main()
  common_word_percent = output_percentages[0]
  rare_word_percent = output_percentages[1]
  uncommon_word_percent = output_percentages[2]
  misspelled_word_percent = output_percentages[3]

  print(f" Percentage of Common Words = {common_word_percent} \n Percentage of Rare Words = {rare_word_percent} \n "
        f"Percentage of Uncommon Words = {uncommon_word_percent} \n Percentage of Misspelled Words = {misspelled_word_percent}")




"""

Console Output when __name__ == '__main__'

 Percentage of Common Words = 61.594 
 Percentage of Rare Words = 18.646 
 Percentage of Uncommon Words = 14.804 
 Percentage of Misspelled Words = 4.957
 
"""



