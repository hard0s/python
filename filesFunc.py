import string

def fileFunc(filename):
    file = open(filename, "r")

    text = file.read()
    for line in string.ascii_lowercase:
        if line in text:
            return "Contains Latin Alphabet"
    
    return "Doesn't contain Latin Alphabet"

filename = str(input("Enter filename: "))
f = fileFunc(filename)
print(f)