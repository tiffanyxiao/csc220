'''problem is that it doesnt find all the possible combinations given that it
increases in increment down the table. solution COULD BE THAT WE REDO THE FUNCTION FOR ALL
COMBINATIONS if they add up to some number greater than the given total

multiprocessing might be a good idea for working with multiple tables at a time?'''

from itertools import combinations

def pantrySums(boxes, n_items, total):
    result = []
    value = 0

    #create a list of lists, index is weight
    pantry = [None]*(total+1)

    for box in boxes:
        if (boxes.get(box) == total):
            result.append(["---"]) #if its complete by itself leave alone
        elif (boxes.get(box) < total and pantry[boxes.get(box)] == None) :
            pantry[boxes.get(box)] = [box]
        elif (boxes.get(box) < total and pantry[boxes.get(box)] != None ):
            pantry[boxes.get(box)].append(box)



    #get all the numbers in a where there is are items attached to the index
    pantry_vals = []
    for i in range(len(pantry)):
        if (pantry[i] != None):
            for box in pantry[i]:
                pantry_vals.append(i)


    #want to include 0 in the table so we need total+1
    #[i][j] where i indicates row and j indicates column
    arrayValues = [["U" for col in range(total+2)] for row in range(len(pantry_vals)+1)]


    #fill all the 0's with "T" because we know it's "T"
    for i in range(len(pantry_vals)):
        arrayValues[i][1] = "T"
        arrayValues[i][0] = pantry_vals[i]




    #fill the first row so that other rows can be filled systematically
    for i in range(2, total+2):
        if(pantry_vals[0] == i):
            arrayValues[0][i] = "T"
        else:
            arrayValues[0][i] = "F"

    for i in range(total+1):
        arrayValues[len(pantry_vals)][i+1] = i-1



    # for i in arrayValues:
    #     print(i)


    #now begin systematically filling in the array:
    for row in range (1,len(pantry_vals)):
        for col in range (2,total+2):

            if (arrayValues[len(pantry_vals)][col] < pantry_vals[row]):
                if (arrayValues[row-1][col] == "T"):
                    arrayValues[row][col] = "T"
                else:
                    arrayValues[row][col] = "F"

            # elif (arrayValues[len(pantry_vals)][col] == pantry_vals[row]):
            #     arrayValues[row][col] = "T"

            elif (arrayValues[len(pantry_vals)][col] >= pantry_vals[row]):
                #go up and back to the value to find it

                if (arrayValues[row-1][col-pantry_vals[row]]== "T"):
                    arrayValues[row][col] = "T"
                else:
                    arrayValues[row][col] = arrayValues[row-1][col]

    for i in arrayValues:
        print(i[7])


    # #now retracing to get a subset
    # if (arrayValues[len(pantry_vals)-1][total]):
    #     pointer = [len(pantry_vals)-1, total]
    #
    #     #while my column is 0
    #     while(pointer[1]!=0):
    #         while(arrayValues[pointer[0]][pointer[1]] and pointer[0] > 0):
    #             pointer = [pointer[0]-1, pointer[1]]
    #
    #
    #         result.append(pantry[pantry_vals[pointer[0]+1]])
    #         value += pantry_vals[pointer[0]+1]
    #
    #         print(pointer[1])
    #         pointer = [pointer[0], pointer[1]-pantry_vals[pointer[0]]]
    #
    #
    #


    print(value, "the sum")
    return result

def main():
    boxes = { "chips":2, "detergent":3, "cereal":7,"pepsi":8, "chaps":10}
    #boxes = {"pepsi":55, "chips":25, "detergent":30, "cereal":15}
    num_boxes = len(boxes)
    total = 11
    fullbox = pantrySums(boxes, num_boxes, total)
    print(fullbox, "fullbox")

main()
