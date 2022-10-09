def change():
    if amount < price:
        excess = int(price - amount)
        print("Your money is not enough to purchase this drug. \n You need " + str(excess) + " $ more.")
        print("Sorry we couldn't help you today:(")
    else:
        balance = int(amount - price)
        print("Your balance is " + str(balance) + " $. \n Have a wonderful day;)")


name = input("Enter your name")
print("How can we be of help to you today")
print("1: I would like to purchase a drug \n 2: I would like to speak to the the shop's owner about something else")
option1 = int(input("Select one of these options"))
price = 35
if option1 == 1:
    drug = input("Enter the name of the drug you want to purchase")
    print("Is " + drug + " the drug you want to purchase")
    print("1:Yes \n 2: I made a mistake")
    option2 = int(input("Select one of these options"))
    if option2 == 1:
        amount = int(input("Enter the amount you are using to make this purchase"))
        change()

    elif option2 == 2:
        Drug = input("Enter the name of the new drug you want to purchase")
        amount = int(input("Enter the amount you are using to make this purchase"))
        change()

elif option1 == 2:
    print("We will get the shop's attendant to speak to you soon:)")
