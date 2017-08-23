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


file = open('testinput.txt', 'r')
lines = []

for line in file:
    lines.append(line)
file.close()

testSize = 0
dataFlag = False
directLocation = 0

"""
reads the lines from the 'direct' line, and counts the amount of lines with 0.0000000
to find the size of the test
"""
def getTestSize(linesList, start):
    size = 0
    for i in range(start, len(linesList)):
        tempLine = linesList[i].split()
        if (tempLine[2] == "0.000000000"):
            size+= 1
        else:
            break
    print(size)
    return size


for i in range(0, len(lines)):
    if (lines[i] == 'Direct\n'):
        #add the line before, move Direct by 3 spaces
        lines[i] = "   " + lines[i]
        directLocation = i
        dataFlag = True
        testSize = (2 * getTestSize(lines, i + 1))

    elif(dataFlag):
        if(testSize > 0):
            lines[i] = lines[i].strip('\n') + "\t\t\tF   F   F\n"
            testSize -= 1
        else:
            lines[i] = lines[i].strip('\n') + "\t\t\tT   T   T\n"

lines.insert(directLocation, "Selective Dynamics\n")

fileOut = open('testOutput.txt', 'w')
for j in range(0, len(lines)):
    fileOut.write(lines[j])
fileOut.close()