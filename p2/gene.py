'''
Authors: Heidi Tsang, Tiffany Xiao, Karen Santamaria
Date: February  15, 2018
Title: Gene Splicing

Given two strings representing snippets of genes (letters ACGT), identify the
shortest string that could contain them both as subsequences.
'''

def print_union(string1, string2, union_result):
    '''print out the result in a pretty format'''
    print("**************************************")
    print("String 1 -", string1)
    print("String 2 -", string2)
    print("shortest string that has both as substring")
    print(union_result, "(" + str(len(union_result)) + ")")
    print("**************************************")

def string_union(string1, string2,substring):
    '''make the shortest string  that contains string1 and string2 as subsequences'''
    union_result = ""
    if string1.endswith(substring):
        union_result = string1+ string2.replace(substring,"")
    else:
        union_result = string2+ string1.replace(substring,"")
    return union_result

def get_overlap(string1, string2, len_string1, len_string2):
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
    overlap_len = 0
    overlap_position = []
    for col in range (0,len_string1):
        for row in range (0,len_string2):
            if matrix[row][col] == 1 and row!=0 and col!=0:
                matrix[row][col] = matrix[row][col] + matrix[row-1][col-1]
                if matrix[row][col]>overlap_len:
                    overlap_len = matrix[row][col]
                    overlap_position = [row,col]


    large_share = 0
    large_share_pos = []

    for i in range(len(matrix)):
        if (large_share < matrix[i][len_string1-1]):
            current_pos = [i, len_string1-1]
            keep_going = True

            while (current_pos[0] != 0 and keep_going):
                current_pos = [current_pos[0]-1, current_pos[1]-1]
                if (matrix[current_pos[0]][ current_pos[1]] == 0):
                    keep_going = False

            if (keep_going):
                large_share = matrix[i][len_string1-1]
                large_share_pos = [i,len_string1-1]



    for i in range(len(matrix[len_string2-1])):
        if(large_share < matrix[len_string2-1][i]):
            current_pos = [len_string2-1,i]
            keep_going = True
            while(current_pos[1] != 0 and keep_going):
                current_pos = [current_pos[0]-1, current_pos[1]-1]
                if (matrix[current_pos[0]][ current_pos[1]] == 0):
                    keep_going = False
            if (keep_going):
                large_share = matrix[len_string2-1][i]
                large_share_pos = [len_string2-1, i]


    for item in matrix:
        print(item)

    print("largest shared positon", large_share_pos)
    print("largest sharted size", large_share)




    #construct the substring
    if (large_share_pos):
        overlap = string1[large_share_pos[1]]
        for l in range(1, overlap_len):
            overlap = string1[large_share_pos[1]-l]+overlap


    else:
        overlap = ""


    return overlap




def main():
    gene_lst = ["A","C","T","G"]
    #test cases


    string1 = "AATCG"
    string2 = "GTTCG"
    # string1 = input("Input the first sequence" + "\n")
    # for l in string1:
    #     if (l not in gene_lst):
    #         raise ValueError('String1 is not a gene')
    #
    # string2 = input("Input the second sequence" + "\n")
    # for l in string2:
    #     if (l not in gene_lst):
    #         raise ValueError('String2 is not a gene')

    substring = get_overlap(string1,string2, len(string1), len(string2))
    print_union(string1,string2,string_union(string1,string2, substring))

main()
