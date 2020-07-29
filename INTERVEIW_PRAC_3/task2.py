import timeit
from task1 import HashTable

# Part 1

def load_dictionary(hash_table, filename):
    """
    function which reads a file 'filename' containing one word per line,
    and adds each word to hash_table with integer 1 as the associated data.
    :param hash_table: an instance of class HashTable passed as a parameter.
    :param filename: the filename of the file to be read.
    :return:
    """

    file = open(filename)
    lines = file.readlines() # Read lines of file
    start = timeit.default_timer()
    for line in lines:
        hash_table.insert(line.rstrip(),1) # remove whitespace
        if timeit.default_timer() - start > 5: # if time taken exceeds 5 seconds, break out of the loop
            break
    file.close()

# h_table = HashTable()
# load_dictionary(h_table,'english_small.txt')
# print(h_table.count)


def dictionary_function():
    """
    Run the loac dictioary function for 3 files "english_small.txt", "english_large.txt","french.txt"
    and calculate the time taken for load dictionary to run for each file, for a combination  of HashBase and
    TableSize.
    Then print the values of HashBase, TableSize and corresponding time in a table in the console.
    :return:
    """

    hash_base_values = [1, 27183, 250726]
    table_size_values = [250727, 402221, 1000081]
    filename = ["english_small.txt", "english_large.txt","french.txt"]

    for file in filename:
        filename = file
        print("\n\n" + str(filename) + "\n")

        b_str = "b"
        table_size_str = "TABLESIZE"
        time_str = "Time (s)"
        print ("%-15s %-15s %-15s" % (b_str, table_size_str, time_str))

        #calculate the time taken for load dictionary to run for each file, for a combination  of HashBase
        for hash_base in hash_base_values:
            for table_size in table_size_values:
                hash_table = HashTable(table_size, hash_base)
                start = timeit.default_timer()
                load_dictionary(hash_table, file)
                time = timeit.default_timer() - start # calculate the time taken
                time = round(time, 6)
                if time > 3:
                    time = "TIMEOUT"
                # print the values of HashBase, TableSize and corresponding time in a table
                print("%-15s %-15s %-15s " % (str(hash_base) ,str(table_size),str(time) ))




if __name__ == '__main__':
   dictionary_function()



"""
english_small.txt

b               TABLESIZE       Time (s)       
1               250727          TIMEOUT         
1               402221          TIMEOUT         
1               1000081         TIMEOUT         
27183           250727          0.398941        
27183           402221          0.400013        
27183           1000081         0.409856        
250726          250727          TIMEOUT         
250726          402221          0.402139        
250726          1000081         0.420613        


english_large.txt

b               TABLESIZE       Time (s)       
1               250727          TIMEOUT         
1               402221          TIMEOUT         
1               1000081         TIMEOUT         
27183           250727          1.142008        
27183           402221          1.026428        
27183           1000081         0.95652         
250726          250727          TIMEOUT         
250726          402221          1.088031        
250726          1000081         1.020499        


french.txt

b               TABLESIZE       Time (s)       
1               250727          TIMEOUT         
1               402221          TIMEOUT         
1               1000081         TIMEOUT         
27183           250727          1.297143        
27183           402221          1.11623         
27183           1000081         1.081901        
250726          250727          TIMEOUT         
250726          402221          1.110449        
250726          1000081         1.062601        

Process finished with exit code 0




Explaination:

There are 9  HashBase (b) and TableSize combinations. 
We record the varying ammount of tme taken to insert words into the HashTable of each of the 9 combinations of 
HashBase and TableSize. 
The combinations of TableSize and HAshBAse that take longer than 10 seconds to complete are recorde with a TimeOut message
When the HashBase is small (eg. 1) , and TableSize is increasingly larger, it takes incresing larger ammounts of time for 
all the words to be inserted into the HashTable, thus resulting in a TimeOut (when time increases more than present Timeout period)
This longer ammount of time is because there aew many collisions and hence linear probing is used to solve these collisions. 
Also,since the HashBase is small the possibilities for unique hash values is limited. 
Therefore the probability of keys many elements hashing to the same value, is extremely high, resulting in more collisions.   
This is made evident for when  HashBase is 1 and TableSize is increasingly larger, the execution always TimesOut.
Therefore having larger HashBase makes it more feasible to create unique hash values, for thr positions of tuples.


The number of collisions is also impacted by the TableSize. Because for the universal HashFunction the number of collisions 
is inversely proportional to TableSize == 1/TableSize. Therefore to minimize collision the TableSize should be large and a prime number. 
When TableSize is Large and Prime, fewer collisions take place therefore smaller execution time. 
This is made evident when HashBase is 27183 and TableSize is increasingly larger, and as TableSize increases the execution time drops 
since there are fewer collisions. 

When HashBase = 250726 and TableSize = 250727, this times out since the HashBase and TableSize are very close and hashbase is not a prime.
Also when hashBase = 250726 and Tablesize is larger, the time is not very much less compared to other times for same TableSize 
this is because the HashBase is not prime. 
 
"""

