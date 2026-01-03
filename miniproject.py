import random

target = random.randint(1,100)

while True:
    userChoice =int(input("Guess the target or Quit:"))
    if(userChoice == "Quit"):
        break
    userChoice =int(userChoice)

    if(userChoice == target):
        print("Success:Correct guess ..")
        break
    elif(userChoice<target):
        print("guess a bigger number")
    else:
        print("guess smaller number u have guessed a very big number")
        

   
   
print("____Game over___")
