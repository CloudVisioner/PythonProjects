from selectors import SelectSelector

print("Welcome to online pizza order.")
type = input("What type of pizza would you like to choose Small, Medium or Large? ").lower()
Pepperoni  = input("Would you like to add pepperoni? type y or n. ")
cheese = input("What about extra cheese? y or n. ")
Bill = 0

if type == "small":
    Bill += 15
elif type == "medium":
    Bill += 20
elif type == "large":
    Bill += 25
else:
    print("You typed the wrong input!")

if Pepperoni == "y":
    if type == "small":
        Bill += 2
    else:
        Bill +=3

if cheese == "y":
    Bill += 1





print("Your total cost for pizza is $" + str(Bill))

input("Please click the button enter to exit...")


