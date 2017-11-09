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
