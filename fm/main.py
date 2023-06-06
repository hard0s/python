import os

def main():
    e = str(input("Enter command: "))
    if e == 'HELP' or e == 'help':
        print("touch")
        print("mkdir")
        print("cd")
        print("ls")
        print("pwd")
        print("rm")
        print("rmdir")
        print("move")
        print("rename")
    elif e == "touch":
        fp = open(e, 'x')
        fp.close()
    elif e == "mkdir":
        x = str(input("Enter name: "))
        os.mkdir(x)
    elif e == "cd":
        x = str(input("Enter name: "))
        os.chdir(x)
    elif e == "rmdir":
        x = str(input("Enter name: "))
        os.rmdir(x)
    elif e == "rm":
        x = str(input("Enter name: "))
        os.remove(x)
    elif e == "move":
        x = str(input("Enter file name: "))
        x1 = str(input("Enter new file name: "))
        os.replace(x, x1)
    elif e == "rename":
        x = str(input("Enter file name: "))
        x1 = str(input("Enter new file name: "))
        os.rename(x, x1)
    elif e == "pwd":
        print ("Current DIR:", os.getcwd())
    elif e == "ls":
        os.listdir()
    else:
        print ("Unknown command:", e)

if __name__ == '__main__':
    while True:
        main()