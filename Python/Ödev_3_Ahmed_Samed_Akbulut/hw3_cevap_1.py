import random as rnd
sayý = rnd.randint (0,10000)
result = False
while result!= True:
    a=input("Enter the number (or write ""end"" if you want to exit) :")
    if a == "end":
        print("Game Over")
        break
    a = int(a)
    if a==sayý:
        print("Congrats!! You won!!")
        result=True
    elif a > sayý :
        print("Your number is too high")
    elif a < sayý :
        print("Your number is too low")
