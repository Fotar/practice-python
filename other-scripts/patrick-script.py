"""
Output editing script for Patrick.
inputs: file name - might add support for many files later
outputs: file that has been edited, as long as I don't have to rename this should be simple as.

author: Marion Daly-Andrusiak
description:
    Takes an input file of specific format and adds T and F entries to the end of each row of output data.
    F entries cover the first 2 sets of data, T entries cover the rest.
    Also adds a row that contains the text 'Selective Dynamics' to be added to the top of the data output.
    Shifts the line that says 'direct' by 3 spaces
"""
"""
reads the lines from the 'direct' line, and counts the amount of lines with only zeroes
to find the size of the test
"""
def getTestSize(linesList, start):
    size = 0
    for i in range(start, len(linesList)):
        tempLine = linesList[i].split()
        if (checkZeroLine(tempLine[2])):
            size+= 1
        else:
            break
    print(size)
    return size

"""
checks to see if an entry is only zeroes and periods, this is expandable for any
amount of sig figs
"""
def checkZeroLine(entry):
    for i in range(0, len(entry)):
        if entry[i] != '0' and entry[i] != '.' and entry[i] != '\n':
            return False
    return True

inputFile = "testinput.txt"
file = open(inputFile, 'r')
lines = []

for line in file:
    lines.append(line)
file.close()

testSize = 0
dataFlag = False
directLocation = 0




for i in range(0, len(lines)):
    if (lines[i] == 'Direct\n'):
        #add the line before, move Direct by 3 spaces
        lines[i] = "   " + lines[i]
        directLocation = i
        dataFlag = True
        testSize = (2 * getTestSize(lines, i + 1))

    elif(dataFlag):             #if we're up to the data output section
        if(testSize > 0):       #this inserts all the F rows, and counts down
            lines[i] = lines[i].strip('\n') + "\t\t\tF   F   F\n"
            testSize -= 1
        else:                   #once the counter for the F rows is up, put in all the T rows
            lines[i] = lines[i].strip('\n') + "\t\t\tT   T   T\n"

lines.insert(directLocation, "Selective Dynamics\n")
#insert the selective dynamics row at the end so it doesn't muddle up the lines array order

fileOut = open('testOutput.txt', 'w')   #write all the changes, change this to inputFile variable
for j in range(0, len(lines)):          #when Patrick is happy with the script
    fileOut.write(lines[j])
fileOut.close()
