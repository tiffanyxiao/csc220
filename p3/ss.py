'''problem is that it doesnt find all the possible combinations given that it
increases in increment down the table. solution COULD BE THAT WE REDO THE FUNCTION FOR ALL
COMBINATIONS if they add up to some number greater than the given total
multiprocessing might be a good idea for working with multiple tables at a time?
need to work on retracing but otherwise its okay!!
'''


def prime_pantry(boxes, n_items, total):
    result = []

    #recreate pantry where index is the weight of the item and each index holds
    #a list of items
    pantry = [None]*(total+1)

    #fill up the pantry with boxes
    for box in boxes:
        if (boxes.get(box) == total):
            print("only this box needed:", box)
            return
             #if its complete by itself leave alone
        elif (boxes.get(box) < total and pantry[boxes.get(box)] == None):
            pantry[boxes.get(box)] = [box]
        elif(boxes.get(box) < total and pantry[boxes.get(box)] != None):
            pantry[boxes.get(box)].append(box)


    #find all the weights in the pantry
    pantry_vals = []
    for i in range(len(pantry)):
        if (pantry[i] != None):
            for box in pantry[i]:
                pantry_vals.append(i)


    #p_v_total is a 2d array. rows indicate pantry_vals and the columns
    #are values up to "total"
    #[i][j] where i indicates row and j indicates columns
    arrayValues = [["---" for col in range(total+1)] for row in range(len(pantry_vals))]


    #fill all the 0's with true because we know it's true
    for i in range(len(pantry_vals)):
        arrayValues[i][0] = True

    #fill the first row so that other rows can be filled systematically
    for i in range(1, total+1):
        if(pantry_vals[0] == i):
            arrayValues[0][i] = True
        else:
            arrayValues[0][i] = False

    #fill in 2d array
    for row in range (1,len(pantry_vals)):
        for col in range (1, total+1):

            #if value of pantry greater than column its impossible to add up to it
            #so get value from row above
            if (pantry_vals[row] > col ):
                arrayValues[row][col] = arrayValues[row-1][col]

            #if value for pantry less than column then check if it is possible to add up to
            elif (pantry_vals[row] < col):
                if (arrayValues[row-1][col]):
                    arrayValues[row][col] = arrayValues[row-1][col]
                else:
                    arrayValues[row][col] = arrayValues[row-1][col-pantry_vals[row]]

            #if value for pantry is equal then we know it is possible to add to
            elif (pantry_vals[row] == col):
                arrayValues[row][col] = True



    #pointer travels through 2d array to reach either row 0 or column 0
    pointer = [len(pantry_vals)-1, total]

    #if cant add up to total then print closest
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
                #if 0 row has been reached it is the end
            break;

        valbfor = pointer[0]+1
        result.append(pantry_vals[pointer[0]+1])
        pointer[1]=pointer[1]-pantry_vals[pointer[0]+1]

    listbox = []
    for item in result:
        listbox.append(pantry[item])
    print()
    print("values:", result, "sum result: ",sum(result),"desired total: ", total)
    print("boxes:", listbox)
    print()

    return arrayValues[len(pantry_vals)-1][total]


def main():
    boxes = {"pepsi":55, "chips":25, "detergent":30, "cereal":15, "cake":15}
    num_boxes = len(boxes)

    for i in range(25, 126):
        prime_pantry(boxes, num_boxes, i)

main()

#prime_pantry(ast.literal_eval(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
