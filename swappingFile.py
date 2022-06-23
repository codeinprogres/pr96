
def swapFileData():
    hi = input("Write file here: ")
    swap = input("Write file swap here: ")
    
    with open('sample1.txt', 'r') as a:
        data_a = a.read()
    
    with open('sample2.txt', 'r') as a:
        data_b = a.read()

    with open('sample1.txt', 'w') as a:
        a.write(data_b)

    with open('sample1.txt', 'w') as a:
        a.write(data_a)

swapFileData()