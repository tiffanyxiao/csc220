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
#import numpy as np
def make_shortest_string(string1, string2,substring):
    shortest_string = ""
    if string1.endswith(substring):
        shortest_string = string1+ string2.replace(substring,"")
    else:
        shortest_string = string2+ string1.replace(substring,"")
    return shortest_string
def intersection(string1, string2, len_string1, len_string2):
    #fill in everything with zeros
    matrix = [[0 for col in range(len_string1)] for row in range(len_string2)]
    #string1 is associated with horizontal diraction
    #string2 is associated with vertical direction

    #fill in 1's with matches
    for col in range (0,len_string1):
        for row in range (0,len_string2):
            if (string1[col] == string2[row]):
                matrix[row][col] = 1
    #for every cell in the matrix, add the value of the upper-reight cell to the current cell
    #so the value of the cells will be the number of cosecutive match if there is any
    largest_count = 0
    index_of_largest = []
    for col in range (0,len_string1):
        for row in range (0,len_string2):
            if matrix[row][col] == 1 and row!=0 and col!=0:
                matrix[row][col] = matrix[row][col] + matrix[row-1][col-1]
                if matrix[row][col]>largest_count:
                    largest_count = matrix[row][col]
                    index_of_largest = [row,col]

    #construct the substring
    overlap = string1[index_of_largest[1]]
    for l in range(1, largest_count):
        overlap = string1[index_of_largest[1]-l]+overlap
    return overlap



def main():
    str_lst = ["A","C","T","G"]
    string1 = "AACCTGT"
    string2 = "CTGTACG"
    substring = intersection(string1,string2, len(string1), len(string2))
    short = make_shortest_string(string1,string2, substring)
    print(short)
main()
