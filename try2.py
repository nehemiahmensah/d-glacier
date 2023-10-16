import getpass

def  main_menu(home):
     print("\n MENU \n 1. Make Deposit \n 2. Withdrawal \n 3. Transfer Money \n 4. Check Balance\n 5. Financial Statement")
    #  while True:
    #     try:
    #         home = input("Enter optionsm (number only): ")
    #         home = int(home)
    #         break
    #     except ValueError:
    #         print ("Invalid input")
     return ("")

def menu(home2):
    print("\n 1. Return to Main Menu \n 2. Exit")
    while True:
        try:
            home2 = input("Enter option (number only): ")
            home2 = int(home2)
            break
        except ValueError:
            print ("Invalid Input")
    while True:
        try:
            if home2 == 1:
                print(main_menu(0))
                break
            elif home2 == 2:
                break
        except ValueError:
            print("Invalid Input")
    return ("")
def app(card):
    income.append(card)
    return card
    


#welcome to ussd app
print("\n WELCOME TO SILICON ACCRA INNOVATION SCH. USSD SERVICE \n")
print("\n To proceed create a unique 4-digit passcode -- PLEASE DO NOT START WITH 0(ZERO)")

#this line of code handles exceptions when user enters wrong input for unique code
while True:
    try:
        user_input = getpass.getpass("Enter a 4-digit number : ")
        user_input = int(user_input)
        if 1000 <= user_input <= 9999:
            print("Thank You!. Do not share this code with anyone.")
            break
        else:
            print("Invalid input. Please enter a 4-digit number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# this code prints menu for the user to make an option
print(main_menu(4))

#this code validates the input for selecting an item on the menu
while True:
    try:
        choice = input("Enter option (number only): ")
        choice = int(choice)
        break
    except ValueError:
        print ("Invalid input")
while True:
    if choice == 1:
        try:
            card = int(input("Enter 12 digit code on the scratch card: "))
            if 100000000000 <= card <= 999999999999:
                print("\n Thank You!! Deposit Successful. ")
                print(menu(0))

                break
            else: print("Invalid Card")
        except ValueError:
            print("Invalid Input")      


