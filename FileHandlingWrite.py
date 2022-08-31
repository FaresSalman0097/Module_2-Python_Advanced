# this function will overwrite the existing file and create a new file
'''file = open("C:/Users/ibrah/PycharmProjects/FileHandlingTestFile.txt",'w')
file.write("This will add new line")
file.write("\nWhenever we use write option it will oevrwrite the existing file")
file.write("\nEven when the file is not created, if you use write the new file will be created")
file.close()'''

# using "with" block
with open("C:/Users/ibrah/PycharmProjects/FileHandlingTestFile_3.txt","w") as file:
    file.write("Hello, Eppadi Irukinga")


# Advantage of "with" block is we do not need to mention file.close() explicitly
