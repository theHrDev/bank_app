
import random
class User:
    def __init__(self):
        self.users = {}
        
    def create_account(self,firstname,lastname,email,password):
        if email in self.users:
            return "User with the email already exist"
        account_number = random.randint(10**9,10**10-1)
        new_user = {"firstname":firstname,"lastname":lastname,"email":email,"password":password,"account_number":account_number}
        self.users[email] = new_user
        return "Account successfully created"
    
    def view_single_user(self,email):
        if not self.users[email]:
            return "No user with the email"
        return self.users[email]
    
    def login(self,email,password):
        pass
        
    def view_users(self):
        if not self.users:
            return "No user found"
        return self.users
        
        
class Authenticated_Actions:
    def __init__(self):
        pass
    

def bank_app():
    user = User
    while True:
        print("Welcome to Easy Bank,wishing you an easy banking with us")
        print("------- 1. Open Account ---------")
        print("------- 2. Login ---------")
        print("------- 3. View Single User ---------")
        print("------- 4. View All Users ---------")
        print("------- 5. Exit ---------")
        
        choice = input("\n Enter a menu to get started: ")
        
        if choice == "1":
            firstname = input("Enter your first name: ")
            lastname = input("Enter your last name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            print(user.create_account(email=email,lastname=lastname,firstname=firstname,password=password))
            
        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            print(user.login(email=email,password=password))
            
        elif choice == "3":
            email = input("Enter your email: ")
            print(user.view_single_user(email=email))
            
        elif choice == "4":
            print(user.view_users())
        
        elif choice == "5":
            break
        
        else:
            print("Invalid Input")
    
    