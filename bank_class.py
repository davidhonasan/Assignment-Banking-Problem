# For function who needs to go back to "main" in other files.
def login():
    from interface import login  # Configure why do file dari atas lagi
    login()


def menu():
    from interface import menu  # Configure why do file dari atas lagi
    menu()


def admin_menu():
    from interface import admin_menu  # Configure why do file dari atas lagi
    admin_menu()

class Bank():
    customers_list = []

    def __init__(self):
        self.__name = "Bank David"

    def add_customer(self):
        print("\n##### NEW CUSTOMER #####"
              "\nPlease input your")
        y = input("First Name\t:").lower()
        z = input("Last Name\t:").lower()
        x = str(input("Password\t:"))
        x1 = str(input("Confirm Password\t:"))
        if x == x1:
            w = len(self.customers_list)
            self.customers_list.append(Customer(str(w), x, y, z))
            Account.money_list.append(Account(0))
            print("\nYou have created an account. Please login with id:", w)
        else:
            print("\nPassword isn't match.")

    def get_num_of_customers(self):  # get total of customer, using list? use return
        x = len(self.customers_list) - 1
        return x

    def get_customer(self):  # print customer info. using index?. create admin acc?
        pass


class Customer(Bank):
    id_logged_in = -100  # ID who login
    def __init__(self, num=str(), password=str(), first="", last=""):
        super().__init__()
        self.__id = num
        self.__password = password
        self.__first_name = first
        self.__last_name = last

    def return_customers(self):
        print("\n##### OLD CUSTOMER #####"
              "\nPlease input your")
        x = input("ID\t:")
        y = input("Password\t:")
        for i in self.customers_list:
            if x == "0":  # ADMIN
                if y == i.__password:
                    print("You've logged in with ID:", i.__id)
                    Customer.id_logged_in = i.__id
                    admin_menu()
                else:
                    print("Wrong Password!")
                    login()
            elif x == i.__id:  # OTHER
                if y == i.__password:
                    print("You've logged in with ID:", i.__id)
                    Customer.id_logged_in = i.__id
                    menu()
                else:
                    print("Wrong Password!")
                    login()
        print("Wrong ID!")  # IF ID NOT FOUND
        login()

    def print_all_customers(self):
        print("##### LIST OF CUSTOMERS #####"
              "\nYou have", Bank().get_num_of_customers(), "customer.")
        for i in Bank.customers_list:
            print("{0}.\t{1}\t{2}".format(i.__id, i.__first_name, i.__last_name))

    def get_id(self):
        return self.__id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name




class Account(Customer):
    money_list = []
    def __init__(self, balance=0):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self):
        i = int(Customer.id_logged_in)
        self.money_list[i-1].__balance = self.__balance

    def set_self_balance(self):
        i = int(Customer.id_logged_in)
        self.__balance = self.money_list[i - 1].__balance

    def deposit(self):
        amt = input("How much money you want to deposit?\n")
        if amt.isdigit() is True:
            self.set_self_balance()
            self.__balance += int(amt)
            print("You have deposited", amt, "\nYour balance is now", self.__balance)
            self.set_balance()
        else:
            print("[ERROR] Typed amount is not digits.")


    def withdraw(self):
        amt = input("How much money you want to withdraw?")
        if amt.isdigit() is True:
            self.set_self_balance()
            if int(amt) <= self.__balance:
                self.__balance -= int(amt)
                print("Withdraw success. You have withdrew", amt, "\nYour balance is now", self.__balance)
                self.set_balance()
            else:
                print("Sorry, you can't withdraw money more than your account balance.")
                self.withdraw()
        else:
            print("[ERROR] Typed amount is not digits.")

    def get_account(self):  # printing account info
        i = int(Customer.id_logged_in)
        print("\n##### ACCOUNT INFO #####"
              "\nID:", Bank.customers_list[i].get_id(),
              "\nFirst name:", Bank.customers_list[i].get_first_name(),
              "\nLast name:", Bank.customers_list[i].get_last_name(),
              "\nBalance:", self.money_list[i-1].get_balance())

Bank.customers_list.append(Customer("0", "admin", "Bank", "Administrator"))  # ADMIN ACC
