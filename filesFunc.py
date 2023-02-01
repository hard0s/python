import re

def fileFunc(filename):
    file = open(filename, 'r')
    text = file.read()
    latinAlphabet = re.compile('[a-zA-Z]+')
    for i in range(len(text)):
        if text[i] == latinAlphabet:
            returnValue = "File contains Latin Alphabet"
            break
        else:
            returnValue = "File don't contains Latin Alphabet"
    file.close()
    print(returnValue)

filename = str(input("Enter filename: "))
fileFunc(filename)