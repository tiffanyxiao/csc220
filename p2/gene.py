'''
Authors: Heidi Tsang, Tiffany Xiao, Karen Santamaria
Date: February  15, 2018
Title: Gene Splicing

Given two strings representing snippets of genes (letters ACGT), identify the
shortest string that could contain them both as subsequences.
'''

# def print_union(string1, string2, union_result):
#     '''print out the result in a pretty format'''
#     print("**************************************")
#     print("String 1 -", string1)
#     print("String 2 -", string2)
#     print("shortest string that has both as substring")
#     print(union_result, "(" + str(len(union_result)) + ")")
#     print("**************************************")
#
# def string_union(string1, string2,substring):
#     '''make the shortest string  that contains string1 and string2 as subsequences'''
#     union_result = ""
#     if string1.endswith(substring):
#         union_result = string1+ string2.replace(substring,"")
#     else:
#         union_result = string2+ string1.replace(substring,"")
#     return union_result

def get_overlap(string1, string2, len_string1, len_string2):
    '''find the substring that appear in both strings'''


    if (string1 in string2):
        return string2

    elif (string2 in string1):
        return string1

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
    # overlap_len = 0
    # overlap_position = []
    for col in range (0,len_string1):
        for row in range (0,len_string2):
            if matrix[row][col] == 1 and row!=0 and col!=0:
                matrix[row][col] = matrix[row][col] + matrix[row-1][col-1]
                # if matrix[row][col]>overlap_len:
                #     overlap_len = matrix[row][col]
                #     overlap_position = [row,col]


    large_share = 0
    large_share_pos = []

    for i in range(len(matrix)):
        if (large_share <= matrix[i][len_string1-1]):
            current_pos = [i, len_string1-1]
            keep_going = True
            while (current_pos[0] != 0 and keep_going):
                current_pos = [current_pos[0]-1, current_pos[1]-1]
                if (matrix[current_pos[0]][ current_pos[1]] == 0):
                    keep_going = False

            if (keep_going):
                if (large_share == matrix[i][len_string1-1]):
                    large_share_pos.append([i,len_string1-1])
                else:
                    large_share = matrix[i][len_string1-1]
                    large_share_pos = [i,len_string1-1]



    for i in range(len(matrix[len_string2-1])):
        if(large_share <= matrix[len_string2-1][i]):
            current_pos = [len_string2-1,i]
            keep_going = True
            while(current_pos[1] != 0 and keep_going):
                current_pos = [current_pos[0]-1, current_pos[1]-1]
                if (matrix[current_pos[0]][ current_pos[1]] == 0):
                    keep_going = False


            if (keep_going):
                if (large_share == matrix[len_string2-1][i]):
                    large_share_pos.append([len_string2-1, i])
                else:
                    large_share = matrix[len_string2-1][i]
                    large_share_pos = [len_string2-1, i]


    for item in matrix:
        print(item)

    print("large share position",large_share_pos)
    print("largest shared",large_share)



    if (large_share == 0):
        return [string1 + string2, string2 + string1]
    # if string is somewhere inbetween (either in front or in middle)
    if (large_share_pos[1]+1 == len(string2)):
        return[string1[:len_string1-1]+string2]
    elif (large_share_pos[0]+1 == len(string1)):
        return[string2[:len_string2-1]+string1]

    return "" #in case no overlap??






def main():
    gene_lst = ["A","C","T","G"]
    #test cases
    string2 = "ACTG"
    string1 = "TGAC"
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
    print(substring)
    # print_union(string1,string2,string_union(string1,string2, substring))

main()
