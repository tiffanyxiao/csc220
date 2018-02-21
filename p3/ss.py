'''problem is that it doesnt find all the possible combinations given that it
increases in increment down the table. solution COULD BE THAT WE REDO THE FUNCTION FOR ALL
COMBINATIONS if they add up to some number greater than the given total

multiprocessing might be a good idea for working with multiple tables at a time?'''

from itertools import combinations

def pantrySums(boxes, n_items, total):
    result = []

    #create a list of lists, index is weight
    pantry = [None]*(total+1)

    for box in boxes:
        if (boxes.get(box) == total):
            result.append([box]) #if its complete by itself leave alone
        elif (pantry[boxes.get(box)] == None):
            pantry[boxes.get(box)] = [box]
        else:
            pantry[boxes.get(box)].append(box)


    #get all the numbers in a where there is are items attached to the index
    pantry_vals = []
    for i in range(len(pantry)):
        if (pantry[i] != None):
            for box in pantry[i]:
                pantry_vals.append(i)


    #want to include 0 in the table so we need total+1
    #[i][j] where i indicates row and j indicates column
    arrayValues = [["U" for col in range(total+1)] for row in range(len(pantry_vals))]


    #fill all the 0's with true because we know it's true
    for i in range(len(pantry_vals)):
        arrayValues[i][0] = True

    #fill the first row so that other rows can be filled systematically
    for i in range(1, total+1):
        if(pantry_vals[0] == i ):
            arrayValues[0][i] = True
        else:
            arrayValues[0][i] = False

    #now begin systematically filling in the array:
    for row in range (1,len(pantry_vals)):
        for col in range (1,total+1):

            if (col < pantry_vals[row]):
                if (arrayValues[row-1][col] == True):
                    arrayValues[row][col] = True
                else:
                    arrayValues[row][col] = False

            elif (col == pantry_vals[row]):
                arrayValues[row][col] = True

            elif (col > pantry_vals[row]):
                #go up and back to the value to find it

                if (arrayValues[row-1][col-pantry_vals[row]]== True):
                    arrayValues[row][col] = True
                else:
                    arrayValues[row][col] = arrayValues[row-1][col]

    for item in arrayValues:
        print(item)


    #now retracing to get a subset
    if (arrayValues[len(pantry_vals)-1][total]):
        pointer = [len(pantry_vals)-1, total]


        while(pointer[1] > 0 or pointer[0] > 0):
            while(arrayValues[pointer[0]-1][pointer[1]] and pointer[0] >= 0):
                pointer = [pointer[0]-1, pointer[1]]
            pointer = [pointer[0], pointer[1]-pantry_vals[pointer[0]]]
            result.append(pantry[pantry_vals[pointer[0]]])




            # while(arrayValues[pointer[0]][pointer[1]]):
            #     pointer = [pointer[0]-1, pointer[1]]
            # result.append(pantry[pantry_vals[pointer[0]]])
            # pointer = [pointer[0], pointer[1]-pantry_vals[pointer[0]]]



    return result



def main():
    boxes = { "chips":2, "detergent":3, "cereal":7,"pepsi":8, "chaps":10, "chuck":2}
    #doesnt work with chuck = 2 but with chuck = 3 it does
    num_boxes = len(boxes)
    total = 11
    fullbox = pantrySums(boxes, num_boxes, total)
    print(fullbox)





main()
