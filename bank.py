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

def open_account():
    pass
def login():
    pass
def view_user():
    pass

def bank_app(menu):
    print("Welcome to Easy Bank, wishing you a easy banking with us")
    if(menu == "1"):
        open_account()
    elif(menu == "2"):
        login()
    elif(menu == "3"):
        view_user()
    elif(menu == 4):
        exit()
    else:
        print("Unknown Menu")