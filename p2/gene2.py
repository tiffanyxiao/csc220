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


def intersection(string1, string2, len_string1, len_string2):
    #fill in everything with zeros
    matrix = [[0 for col in range(len_string1+1)] for row in range(len_string2+1)]
    #string1 is associated with horizontal diraction
    #string2 is associated with vertical direction



    ##start building matrix todo find a better way to insert letters
    for col in range (len_string1):
        for row in range (len_string2):
            if (row == 0):
                matrix[row][col+1] = string1[col]
            if (col == 0):
                matrix[row+1][col] = string2[row]

    matchList =  []
    #fill in 1's with matches
    for col in range (0,len_string1):
        for row in range (0,len_string2):
            if (matrix[row][col] == matrix[row][0]):
                matrix[row][col] = 1
                #matrix[row][col] = [row,col] #temp
                matchList.append([row,col])
            # else:
            #     matrix[row][col] = [0,0] #temp

    print(matchList)
    help_print(matrix)

    #fill in unused spot
    matrix[0][0] = "-"



    ##end building matrix

    long_str = ""
    long_str_len = 0



def countList(listOfList):
    length = []
    for list in listOfList:
        best_count = 0
        current_count = 0
        for i in list:
            if list[i]==1:
                current_count = current_count+1
                if current_count > best_count:
                    best_count = current_count
            else:
                current_count = 0
        length.append(best_count)

def help_see(matrix):
    '''see how numbers are changed loop by loop through the matrix'''
    for col in range (1,len_string1+1):
        for row in range (1,len_string2+1):
            matrix[row][col] = "-"
            help_print(matrix)

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
