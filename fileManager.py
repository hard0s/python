import os

def filesystem():
    comand = ""
    loop = True
    while loop:
        meh = str(input("What you wonna do: "))
        match (meh):
            case "mkdir":
                comand = str(input("Enter folder name: "))
                os.mkdir(comand)
            case "rmdir":
                comand = str(input("Enter folder name: "))
                os.rmdir(comand)
            case "ls": 
                print(os.listdir())
            case "cd":
                comand = str(input("Enter directory: "))
                os.chdir(comand)
            case "pwd":
                print(os.getcwd())
            case "touch":
                comand = str(input("Enter folder name: "))
                text = open(comand, "w")
            case "write":
                comand = str(input("Enter text: "))
                fname = comand
                text.write(comand)
            case "rename":
                comand = str(input("Enter new file name: "))
                os.rename(fname, comand)
            case "exit":
                loop = False

def main():
    filesystem()

main()