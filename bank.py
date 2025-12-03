
import random
users = []
user = {}
def open_account(firstname,lastname,email,password):
    global user, users
    for existing_user in users:
         if email in existing_user["email"]:
            return "User with the email already exists"
    if int(len(password)) < 8:
        return "Your password must be atleast 8 characters"
    account_number = random.randint(10**9,10**10-1)
    user={"firstname":firstname, "lastname":lastname,"email":email,"password":password,"account_number":str(account_number),"account_balance":500000}
    users.append(user)
    
    return f"Account created successfully"


def login(credentials,password):
    global users

    for existing_users in users:
       if existing_users["email"] == credentials or existing_users["account_number"] == credentials:
           if existing_users["password"] == password:
               return f"Login Successful \n Welcome {existing_users["firstname"]} {existing_users["lastname"]} \n You have #{existing_users["account_balance"]} in your account balance"
                
           return "Invalid credentials"
    
    return "Account not valid"

                
    
def view_user():
    global users
    return users

def bank_app(menu):
    print("Welcome to Easy Bank, wishing you a easy banking with us:")
    if(menu == "1"):
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        email = input("Enter email: ")
        password = input("Enter your password: ")
        print(open_account(firstname,lastname,email,password))
    elif(menu == "2"):
        credentials = input("Enter your email or your account number: ")
        password = input("Enter your password: ")
        print(login(credentials,password))
    elif(menu == "3"):
        print(view_user())
    elif(menu == 4):
        exit()
    else:
        print("Unknown Menu")
        
    repeat = input("Do you want to perform another task?\n1.Yes \n2.No: ")
    if repeat == "1":
        menu = input("Choose a menu to start with us:\n1.Open Account\n2.Login to your account\n3.View User\n4.Exit: ")
        bank_app(menu)
    else:
        exit()
        
menu = input("Choose a menu to start with us:\n1.Open Account\n2.Login to your account\n3.View User\n4.Exit: ")
bank_app(menu)

