# write and read the file at the same time
# Creates the new file
file = open("C:/Users/ibrah/PycharmProjects/FileHandlingTestFile_1.txt",'w+')
print(file.read())
file.write("This is the new file where we created a file and read it")
print(file.read())
file.close()
