# Hardest game ever
# Credits to Aarooshcoding33
# Assets are auto detected

import time
print('The hardest game ever.')
print("Name: Put the food in!")
time.sleep(5)
Fridge = ['Chicken','CatNap','Huge Ice cream','A box full of fruits']
print("You fridge:",Fridge)

Points = []

Places = str(input("Go to Shopping! "))
if Places == "ok" or Places == "Ok":
    Buyer1 = str(input("E to buy a huge packet of cereal: "))
    if Buyer1 == "E":
        print("Succesfully buyed it.")
        time.sleep(4)
        Prompt1 = str(input("E to put in the fridge. (Size: 400px Fridge Size: 4 items can fit) "))
        if Prompt1 == "E":
            print("Removing Huge Ice cream...")
            time.sleep(2)
            Fridge.pop(2)
            Fridge.append("Huge pack of cereal")
            print(Fridge)
            print("Failed!")
            time.sleep(3)
            str(input("Retry? "))
        elif Prompt1 == "No" or Prompt1 == "no":
            print("+5 Points.")
            Points.append(5)
            time.sleep(2)
            print("Would you like to buy a corrupted file in your fridge?")
            Prompt2 = str(input())
            if Prompt2 == "No" or Prompt2 == "no":
                print("+5")
                Points.append(5)
                time.sleep(2)
                print("You won!")
                time.sleep(4)
                print("Just kidding.")
                time.sleep(2)
                Prompt3 = str(input("Put a mega ice in the fridge yes or no: "))
                if Prompt3 == "yes" or Prompt3 == "Yes":
                    Fridge.clear()
                    print(Fridge)
                    Fridge.append("Mega Ice")
                    print(Fridge)
                    time.sleep(3)
                    print("Game Over bud, restart.")
                else:
                    print("+5 Points.")
                    Points.append(5)
                    time.sleep(2)
                    Prompt4 = str(input("You wanna live in the fridge for 51 years? "))
                    if Prompt4 == "no" or Prompt4 == "No":
                        print("That proved you are not stupid.")
                        time.sleep(4)
                        print("+14 Points!! THE END!")
                        Points.append(14)
                        time.sleep(2)
                        print("Total Points:")
                        Total = sum(Points)
                        print(Total)
                    else:
                        print("A stupid move you made, GAME OVER!")
            else:
                print("FAILED!")
else:
    print("You lost!")