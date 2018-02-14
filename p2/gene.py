'''
Objective: given two strings representing snippets of genes (letters ACGT),
identify the shortest string that could contain them both as subsequences.


********************************************
string 1 – AACCTGT     string 2 – CTGTACG
shortest string that has both as substring
AACCTGTACG (length 10)
********************************************

The submission:

successfully reads in a pair of strings
outputs a string that contains both input strings as a subsequence
checks to ensure input is valid before beginning calculation; if not, throws an exception
Second level (2 points)

The submission:

correctly reports the length of the shortest string that contains both input strings
as a subsequence (but possibly fails to return the string itself)
is at least as efficient as the recursive solution i.e. no worse than O(2^n)
Third level (2 points)

The submission:

is more efficient than the recursive solution
correctly returns the shortest string that contains both input strings as a subsequence
*Note* to get efficiency-related points, you must include a brief discussion of the program's efficiency in your README
'''
import numpy as np

def intersection(string1, string2, len_string1, len_string2):
    #fill in everything with zeros
    matrix = [[0 for col in range(len_string1)] for row in range(len_string2)]
    #string1 is associated with horizontal diraction
    #string2 is associated with vertical direction


    #fill in 1's with matches
    for col in range (0,len_string1):
        for row in range (0,len_string2):
            if (string1[col] == string2[row]):
                matrix[row][col] = str(row) + " " + str(col)


    a = np.array(matrix)
    diags = [a[::-1,:].diagonal(i) for i in range(-a.shape[0]+1,a.shape[1])]


    ##end building matrix
    long_str = ""
    long_str_len = 0


    for item in diags:
        if (item[0] != '0' or item[len(item)-1] != '0'):

            count_similar = len([x for x in item if x != '0'])
            if (long_item_len < count_similar):

            #print(item, "counted", count_similar)

    good_diagonals = []
    for item in diags:
        if (item[0] != '0' or item[len(item)-1] != '0'): #cant intersect

            for i in range(1,item-1):
                found_zero = False

                while (!found_zero):
                    good_diagonals.append







def help_print(matrix):
    '''print the matrix is view-friendly way'''
    for i in matrix:
        print(i)

def main():
    str_lst = ["A","C","T","G"]
    string1 = "AACCTGT"
    string2 = "CTGTACG"
    string3 = intersection(string1,string2, len(string1), len(string2))
main()
