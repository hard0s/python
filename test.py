import string

def openFile(filename):
    file = open(filename, "r")

    text = file.read()
    for line in string.ascii_lowercase:
        if line in text:
            return "Contains Latin Alphabet"
    
    return "Doesn't contain Latin Alphabet"

def __main__():
    f = openFile("test")
    print(f)

__main__()