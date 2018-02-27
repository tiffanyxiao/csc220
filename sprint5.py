
def getFactor(num):
    num_lst = []

    while (num != 1):
        for i in range(2, num+1):
            if (num%i == 0):
                num = int(num/i)
                num_lst.append(i)
                break


    return num_lst



def main():


    num_lst = [121, 39, 240, 53]
    a = []

    for num in num_lst:
        print("these are the factors",getFactor(num))




main()
