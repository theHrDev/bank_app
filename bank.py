# 1, Open account
# 2. To login
# 3. Print all user info
# 4. Exit

# 1. firstname
#     lastname
#     email
#     password


# 1234567890
# 1023456789
# 1204
# 2. email/account_number
#     password
#     print("welcome, firstname lastname, you have #50000 in your account")
#     1. To do any other thing
#     2. To logout

# 3. 
# 4. Bye
users = []
user = {}

# 

# print(users["email"])
def open_account(firstname,lastname,email,password):
    global user, users
    for usee in users:
         if email in usee:
            return "User with the email already exists"
    if int(len(password)) < 8:
        return "Your password must be atleast 8 characters"
    user={"firstname":firstname, "lastname":lastname,"email":email,"password":password}
    users.append(user)
    
    return f"{users} Account created successfully"


def login():
    pass
def view_user():
    pass

def bank_app(menu):
    print("Welcome to Easy Bank, wishing you a easy banking with us:")
    if(menu == "1"):
        firstname = input("Enter first name: ")
        lastname = input("Enter last name: ")
        email = input("Enter email: ")
        password = input("Enter your password: ")
        print(open_account(firstname,lastname,email,password))
    elif(menu == "2"):
        login()
    elif(menu == "3"):
        view_user()
    elif(menu == 4):
        exit()
    else:
        print("Unknown Menu")
        
menu = input("Choose a menu to start with us:\n1.Open Account\n2.Login to your account\n3.View User\n4.Exit: ")
bank_app(menu)