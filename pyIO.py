import os
class pyIO:
    def __init__(self, fileName, path=None, data=[]):
        self.fileName = fileName   # the operate file name
        self.path = path           # the path of file
        self.data = data           # the empty list for store data in file

    def writeTxt(self, content):
        file = open(str(self.path) + str(self.fileName),"w")
        file.write(content)
        file.close()
  
    def readTxt(self, separator=None):
        with open(str(self.path) + str(self.fileName)) as file:
            if separator:
                row = file.read().split(separator)
                self.data.append(row)
            else:
                self.data.append(file.readline())
        file.close()
    
    def renameFile(self, newPath=None, newName):
        os.rename(str(self.path) + str(self.fileName), str(newPath) + str(newName))
    
    def removeFile(self):
        os.remove(str(self.path) + str(self.fileName))

if __name__ == '__main__':
    """ This is open file code example. """
    # this is open file example code.
    file = open("testfile.txt","w")
    # these are write file example code.
    file.write("This is your new text file!\n")
    file.write("Why we can do that.\n")
    file.write("Because Magic~")
    # this is close file example code.
    file.close()

    # these are read file example code.
    file = open("testfile.txt","r")
    print "1.these are read file example code."
    print file.read()

    # call a certain number of characters of data in file
    file = open("testfile.txt","r")
    print "2.call a certain number of characters of data in file"
    print file.read(4)

    # return a single line of information in file
    file = open("testfile.txt","r")
    print "3.return a single line of information in file"
    print file.readline()
    
    # return a certain line of information in file
    file = open("testfile.txt","r")
    print "4.return a certain line of information in file"
    print file.readline(3)

    # return all line of information in file
    file = open("testfile.txt","r")
    print "5.return all line of information in file"
    print file.readlines()

    # loop over a file object
    print "6.loop over a file object"
    file = open("testfile.txt","r")
    for line in file:
        print line
    file.close()

    # With Statement
    print "7.With Statement"
    with open("testfile.txt") as file:
        data = file.read()
        print data
    file.close()
