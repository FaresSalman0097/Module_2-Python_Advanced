# write and read the file at the same time
# Does not create the new file
# There should be a existing file
file = open("C:/Users/ibrah/PycharmProjects/FileHandlingTestFile_2.txt",'r+')
print(file.read())
file.write("This is the new file where we created a file and read it")
file.seek(0)
print(file.read())
file.close()