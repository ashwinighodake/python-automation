fd=open("Marvellous.txt","r")
print("Infroation about file:",fd)

print("Contents of whole are")
print(fd.read())

print("Print Reading single line from file")
print(fd.readline())

print("Current file Position is",fd.tell()) #get the current file position
fd.seek(0)   #bring file cursor to initial position

print("Content of Whole file :")
print(fd.read())

fd.close()

fd = open("Marvellous.txt",'a')
fd.write("Python:Automation and Machine Learning \n")
fd.write("Angular: Web development\n")

fd.seek(0)
fd.close()