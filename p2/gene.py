'''
Authors: Heidi Tsang, Tiffany Xiao, Karen Santamaria
Date: February  15, 2018
Title: Gene Splicing

Given two strings representing snippets of genes (letters ACGT), identify the
shortest string that could contain them both as subsequences.
'''

def print_in_format(string1, string2, union_result):
    '''print out the result in a pretty format'''
    print("**************************************")
    print("String 1 -", string1)
    print("String 2 -", string2)
    print("shortest string that has both as substring")
    print(union_result, "(" + str(len(union_result)) + ")")
    print("**************************************")

def make_union_string(string1, string2,substring):
    '''make the shortest string  that contains string1 and string2 as subsequences'''
    union_result = ""
    if string1.endswith(substring):
        union_result = string1+ string2.replace(substring,"")
    else:
        union_result = string2+ string1.replace(substring,"")
    return union_result

def find_overlap(string1, string2, len_string1, len_string2):
    '''find the substring that appear in both strings'''

    #string1 is associated with horizontal diraction
    #string2 is associated with vertical direction
    #everything initially filled in with 0's
    matrix = [[0 for col in range(len_string1)] for row in range(len_string2)]

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
    if (len(index_of_largest)>0):
        overlap = string1[index_of_largest[1]]
        for l in range(1, largest_count):
            overlap = string1[index_of_largest[1]-l]+overlap

    else:
        overlap = ""
    return overlap



def main():
    gene_lst = ["A","C","T","G"]

    string1 = input("The first gene" + "\n")
    string2 = input("The second gene" + "\n")

    for l in string1:
        if (l not in gene_lst):
            raise ValueError('String1 is not a gene')


    for l in string2:
        if (l not in gene_lst):
            raise ValueError('String2 is not a gene')

    substring = find_overlap(string1,string2, len(string1), len(string2))
    print_in_format(string1,string2,make_union_string(string1,string2, substring))

main()
