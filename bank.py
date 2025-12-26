
import random
users = []
user = {}
authenticated_user = {}
def open_account(firstname,lastname,email,password):
    global user, users
    for existing_user in users:
         if email in existing_user["email"]:
            return "User with the email already exists"
    if int(len(password)) < 8:
        return "Your password must be atleast 8 characters"
    account_number = random.randint(10**9,10**10-1)
    user={"firstname":firstname, "lastname":lastname,"email":email,"password":password,"account_number":str(account_number),"account_balance":50000}
    users.append(user)
    
    return f"Account created successfully, your account number is {account_number}"


def login(credentials,password):
    global users

    for existing_users in users:
       if existing_users["email"] == credentials or existing_users["account_number"] == credentials:
           if existing_users["password"] == password:
               global authenticated_user
               authenticated_user = existing_users
               
               return f"Login Successful \n Welcome {existing_users["firstname"]} {existing_users["lastname"]} \n You have #{existing_users["account_balance"]} in your account balance"
                
           return "Invalid credentials"
    
    return "Account not valid"

def view_user():
    global users
    return users



# AUTHENTICATED ACTIONS

def transfer(existing_user):
    recepient_acc_num = input("Enter the account number or email of the recepient: ")
    amount_to_send = int(input("Enter the amount to send: "))
    # print(existing_user["account_balance"])
    if amount_to_send > existing_user["account_balance"]:
        return "Insuufficient account balance"
    password = input("Enter your password: ")
    if password == existing_user["password"]:
        existing_user["account_balance"] = existing_user["account_balance"] - amount_to_send
        return f"{amount_to_send} successfully sent to {recepient_acc_num}"
    
    return "Incorrect Password"
    
    
def check_balance(existing_user):
    return f"Your balance is {existing_user["account_balance"]}"

def change_info(existing_user):
    print("What do you want to change")
    key = input("Enter the key of the value to change: ")
    value = input("Enter the new value: ")
    
    if key not in existing_user:
        return f"Invalid key {key}"
    existing_user[key] = value
    return f"{key} changed successfully to {value}"

def logout():
    print("Bye!!!")
    exit()
        
def autheticated_actions():
    login_menu = input("What do you want to do?\n1.Transfer\n2.Check Balance\n3.Change Info\n4.Logout: ")
    if login_menu == "1":
        print(transfer(authenticated_user))
    elif login_menu == "2":
        print(check_balance(authenticated_user))
    elif login_menu == "3":
        print(change_info(authenticated_user))
    elif login_menu == "4":
        logout()
    else:
        exit()
    repeat = input("Do you want to perform another task?\n1.Yes \n2.No: ")
    if repeat == "1":
        autheticated_actions()
        # menu = input("What do you want to do?\n1.Transfer\n2.Check Balance\n3.Change Info\n4.Logout: ")
    else:
        
        exit()
            
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
        print(autheticated_actions())   
        
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

