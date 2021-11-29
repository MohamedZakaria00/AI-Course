pi=3.14
gravaty=9.8
constant=10
programer ="Mohamed Zakaria"

def add2numbers(x,y):
    print (x+y)
    
    
def askuser():
    answer = input ("Which the best TV show in the world")
    if (answer == "GOT"):
        print ("Correct")
    else:
        print ("Wrong")
def torepresentascciicode():
    string = (input ("Enter the character : "))
    for c in string:
     print("The ASCII value is ", ord(c), end=':')