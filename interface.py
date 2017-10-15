from bank_class import *

b = Bank()
c = Customer()
a = Account()


def welcome():
    print("Welcome to Bank David.\nPlease press the number for the menu you want to select.")
    login()


def login():
    x = input("\n##### LOGIN #####"
              "\n[1]Register New Account"
              "\n[2]Login to your Account"
              "\n[3]Exit\n")
    if x == "1":
        b.add_customer()
        login()
    elif x == "2":
        c.return_customers()
    elif x == "3":
        print("Thank you for using Bank David. Please come again.")
        exit()
    else:
        print("Wrong Command!")
        login()


def admin_menu():
    x = input("\n##### ADMIN MENU #####"
              "\n[1]List of all customer"
              "\n[2]Logout\n")

    if x == "1":
        c.print_all_customers()
        admin_menu()
    elif x == "2":
        print("\nYou've successfully logged out.")
        login()
    else:
        print("Wrong Command!")
        admin_menu()


def menu():
    x = input("\n##### MENU #####"
              "\n[1]Deposit money"
              "\n[2]Withdraw money"
              "\n[3]Account info"
              "\n[4]Logout\n")
    if x == "1":
        a.deposit()
        menu()
    elif x == "2":
        a.withdraw()
        menu()
    elif x == "3":
        a.get_account()
        menu()
    elif x == "4":
        print("\nYou've successfully logged out.")
        login()
    else:
        print("Wrong Command!")
        menu()


if __name__ == '__main__':
    welcome()