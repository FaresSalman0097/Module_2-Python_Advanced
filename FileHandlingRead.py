#Read a file
file = open("C:/Users/ibrah/PycharmProjects/FileHandlingTestFile.txt",'r')
# 'r' represents the mode (i.e) read
# Prints the content of the file method 1
print(file.read())
# method 2
'''for each in file:
    print(each)'''
# Print the values in the form of list
'''print(file.readlines())'''
# Print the data line by line
print(file.readline()) # Reads the first line
print(file.readline()) # Reads the 1st and next lines and so on
# Prints till the value of index
# print(file.read(4))

# Using "with" block
with open("C:/Users/ibrah/PycharmProjects/FileHandlingTestFile.txt") as file:
    data = file.read()
    print(data)