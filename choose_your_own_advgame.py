name = input("Type your name: ")
print("welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left and right. Which way would you like to go? ").lower()

if answer == "left":
   answer = input("You come to river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ").lower()

   if answer == "swim" :
    print("You swim across and were eaten by an aligator.")
     
   elif answer== "walk" :
    print("You walked for many miles, ran out of water and you lost the game.")

   else:
    print("Not a valid answer. You lose." )  


elif answer == "right":
   answer = input("You come to a bridge, it looks wobbly, do you want to cross or head back (cross/back): ").lower()

   if answer == "cross" :
    answer = input("You crossed the bridge and meet a stranger. Do you want to talk? (yes/no): ").lower()

    if answer == "yes" :
     print("You talk to them and they gave you gold. You won!")
     
    elif answer== "no" :
     print("You ignore the stranger and they are offended and you lose.")

    else:
     print("Not a valid answer. You lose." ) 
     
   elif answer== "back" :
    print("You go back and lose.")

   else:
    print("Not a valid answer. You lose." )  

else :
   print("Not a valid answer. You lose.")

print("Thank you for trying", name)
 