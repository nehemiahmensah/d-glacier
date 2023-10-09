import getpass

def main_menu():
    print("\n MENU \n 1. Make Deposit \n 2. Withdrawal \n 3. Transfer Money \n 4. Check Balance\n 5. Financial Statement")
    while True:
        try:
            choice = input("Enter option (number only): ")
            choice = int(choice)
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def menu():
    print("\n 1. Return to Main Menu \n 2. Exit")
    while True:
        try:
            choice = input("Enter option (number only): ")
            choice = int(choice)
            if choice == 1:
                 return choice
            elif choice == 2:
                return choice
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Welcome to USSD app
print("\n WELCOME TO SILICON ACCRA INNOVATION SCH. USSD SERVICE \n")
print("\n To proceed create a unique 4-digit passcode -- PLEASE DO NOT START WITH 0(ZERO)")

# Handle exceptions when user enters wrong input for unique code
while True:
    try:
        user_pin = getpass.getpass("Enter a 4-digit number(pin): ")
        user_pin = int(user_pin)
        if 1000 <= user_pin <= 9999:
            print("Thank You! Do not share this code with anyone.")
            break
        else:
            print("Invalid input. Please enter a 4-digit number.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# THIS IS THE MAIN BODY FOR THE PROGRAM
while True:
    choice = main_menu()
    

    if choice == 1:
        try:
            card = int(input("Enter 12-digit code on the scratch card: "))
            if 100000000000 <= card <= 999999999999:
                print("\n Thank You!! Deposit Successful.")
                return_choice = menu()

                if return_choice == 1:
                    choice
                elif return_choice == 2:
                    print("Exiting program. Goodbye!")
                    break
            else:
                print("Invalid Card")
        except ValueError:
            print("Invalid Input")
    while True:
        if choice == 2:
            try:
                wDraw = float(input("How much do you want to withdraw: "))
                pin = int(input("Enter your pin: "))
                if pin == user_pin:
                    print("Withdrawal Successful")
                    return_choice = menu()  
                    if return_choice == 1:
                        choice
                    elif return_choice == 2:
                        print("Exiting program. Goodbye!")
                    break              
                else: 
                    print("Incorrect Pin")
                
            except ValueError:
                print("Invalid Input. -- for now.lol")
    # Add handling for other menu choices (2, 3, 4, 5) here
