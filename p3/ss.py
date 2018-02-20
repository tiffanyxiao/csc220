
def pantrySums(boxes, n_items, total):


    #create a list of lists bc easier to reference and use than dictionary. index is weight
    pantry = [None]*total
    for box in boxes:
        if (pantry[boxes.get(box)] == None):
            pantry[boxes.get(box)] = [box]
        else:
            pantry[boxes.get(box)].append(box)

    #get all the numbers in a where there is are items attached to the index
    pantry_vals = [i for i in range(len(pantry)) if (pantry[i]!=None)]



    #want to include 0 in the table so we need total+1
    #[i][j] where i indicates row and j indicates column
    arrayValues = [["Fake" for col in range(total+1)] for row in range(len(pantry_vals))]


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
                if (arrayValues[row-1][col]):
                    arrayValues[row][col] = True




    for item in arrayValues:
        print(item)






def main():
    boxes = { "chips":2, "detergent":3, "cereal":5,"pepsi":8, "chaps":2}
    num_boxes = len(boxes)
    total = 11
    pantrySums(boxes, num_boxes, total)




main()
