#Read a file
file = open("C:/Users/ibrah/PycharmProjects/FileHandlingTestFile.txt",'r')
#Prints the content of the file method 1
'''print(file.readlines())'''
#method 2
'''for each in file:
    print(each)'''
#Prints till the value of index
print(file.read(4))