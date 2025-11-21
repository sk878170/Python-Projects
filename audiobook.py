import pyttsx3
def TTS(path):
    with open(path) as book:
        book_text=book.readlines()
        engine = pyttsx3.init()
        for i in book_text:
            engine.say(i)
            engine.runAndWait()
            engine.stop()
    

def create():
    with open("new_file.txt",'w') as f:
        n=input("Enter some text")
        f.write(n)
    print("✅ File 'new_file.txt' created successfully!")

def read(path):
    with open(path,"r") as f:
       content = f.read()
       print(content)

print("Menu:\n1. Create a new file and details to it.\n2. Read a file\n3.Text ot speech")
n=int(input("1/2/3:"))

match n:
    case 1:
        create()
    case 2:
        path=input("Enter the path or name of the file : ")
        read(path)
    case 3:
        path=input("Enter the path or name of the file : ")
        TTS(path)
    case _:
        print("enter a valid input")
        

