import os

Name = "Test1.txt"

i = 1

def greetName(name):
    print("Hello, "+name+" , how are you")
    print("Greet name george")

while i == 1:
    wrte = input()
    
    Hello = open(Name, "a")
    Hello.write(" "+wrte+"\n")
    Hello.close()

    Hello = open(Name, "r")
    print(Hello.read())
    Hello.close()

    os.rename(Name, "New.txt")
    Name = "New.txt"

    greetName(wrte)
    print("\n")
