'''problem is that it doesnt find all the possible combinations given that it
increases in increment down the table. solution COULD BE THAT WE REDO THE FUNCTION FOR ALL
COMBINATIONS if they add up to some number greater than the given total
multiprocessing might be a good idea for working with multiple tables at a time?

need to work on retracing but otherwise its okay!!
'''


def pantrySums(boxes, n_items, total):
    result = []

    #create a list of lists, index is weight
    pantry = [None]*(total+1)

    for box in boxes:
        if (boxes.get(box) == total):
            print("only this box needed:", box)
            return
             #if its complete by itself leave alone
        elif (boxes.get(box) < total and pantry[boxes.get(box)] == None):
            pantry[boxes.get(box)] = [box]
        elif(boxes.get(box) < total and pantry[boxes.get(box)] != None):
            pantry[boxes.get(box)].append(box)


    #get all the numbers in a where there is are items attached to the index
    pantry_vals = []
    for i in range(len(pantry)):
        if (pantry[i] != None):
            for box in pantry[i]:
                pantry_vals.append(i)


    #want to include 0 in the table so we need total+1
    #[i][j] where i indicates row and j indicates column
    arrayValues = [["---" for col in range(total+1)] for row in range(len(pantry_vals))]


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
        for col in range (1, total+1):
            if (pantry_vals[row] > col ):
                arrayValues[row][col] = arrayValues[row-1][col]

            elif (pantry_vals[row] < col):
                if (arrayValues[row-1][col]):
                    arrayValues[row][col] = arrayValues[row-1][col]
                else:
                    arrayValues[row][col] = arrayValues[row-1][col-pantry_vals[row]]

            elif (pantry_vals[row] == col):
                arrayValues[row][col] = True

    #print out table
    # for i in range(total+1):
    #     print(str(i)[-1],"", end = '')

    # print()
    # for item in arrayValues:
    #     for i in item:
    #         if (i):
    #             print("T ", end= '')
    #         else:
    #             print("F ", end = '')
    #     print()



    pointer = [len(pantry_vals)-1, total]

    if not (arrayValues[pointer[0]][pointer[1]]):
        while(arrayValues[pointer[0]][pointer[1]] == False and pointer[1] > 0):
            pointer[1] = pointer[1]-1
        print("closest value is ", pointer[1])
        return False

    while(pointer[1] != 0):
        while(pointer[0] > 0 and arrayValues[pointer[0]][pointer[1]]):
            pointer[0] = pointer[0]-1

        #in the cases where reach top without going left theres two situations
        if (pointer[0] == 0):
            if (pointer[1] not in pantry_vals):
                result.append(pantry_vals[pointer[0]+1])
                result.append(pantry_vals[pointer[0]])
            else:
                result.append(pointer[1])

            break;

        valbfor = pointer[0]+1
        result.append(pantry_vals[valbfor])
        pointer[1]=pointer[1]-pantry_vals[valbfor]

    print(result, "this is result", sum(result), total)
    return arrayValues[len(pantry_vals)-1][total]

    #return result

def main():
    #boxes = { "chips":2, "detergent":3, "cereal":7,"pepsi":8, "chaps":2}
    boxes = {"pepsi":55, "chips":25, "detergent":30, "cereal":15, "cake":15}
    num_boxes = len(boxes)

    for i in range(25, 126):
        pantrySums(boxes, num_boxes, i)

main()
