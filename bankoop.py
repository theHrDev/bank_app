
import random
class User:
    def __init__(self):
        self.users = {}
        self.autheticated_user = {}
    def create_account(self,firstname,lastname,email,password):
        if email in self.users:
            return "User with the email already exist"
        account_number = random.randint(10**9,10**10-1)
        new_user = {"firstname":firstname,"lastname":lastname,"email":email,"password":password,"account_number":account_number,"account_balance":50000}
        self.users[email] = new_user
        return f"Account successfully created, your account balance is {new_user['account_number']} and your account has been credited with $50000 bonus"
    
    def view_single_user(self,email):
        if not self.users[email]:
            return "No user with the email"
        return self.users[email]
    
    def login(self,email,password):
        if email not in self.users:
            return "Invalid credentials"
        else:
            intended_user_details = self.users[email]
            if password == intended_user_details[password] and email == intended_user_details[email]:
                self.autheticated_user = self.users[email]
                
                return "Login Successfully"
            else:
                return "Invalid Credentials"
        
        
    def view_users(self):
        if not self.users:
            return "No user found"
        return self.users
        
        
class Authenticated_Actions(User):
    def __init__(self):
        super().__init__()
        
    def transfer(self,recepient_acc_num,amount_to_send,password):
        if amount_to_send > self.autheticated_user["account_balance"]:
            return "Insufficient Fund"
        else:
            if password == self.autheticated_user["password"]:
                self.autheticated_user["account_balance"] = self.autheticated_user["account_balance"] - amount_to_send
                return f"{amount_to_send} successfully sent to {recepient_acc_num}"
            
            else:
                return "Incorrect password"
            
    def check_balance(self):
        return f"Your account balance is {self.autheticated_user["account_balance"]}"
    
    def edit_info(self,key,value):
        if key not in self.autheticated_user:
            return f"No key with the input key, {key}"
        else:
            self.autheticated_user[key] = value
            return f"Edited successfully, your details is now {self.autheticated_user}"
        
    def logout(self):
        self.autheticated_user = {}
        return "Logout successfully"
   
    

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
            auth_user_action = Authenticated_Actions()
            while True:
                print("------- 1. Make Transfer ---------")
                print("------- 2. Check Balance ---------")
                print("------- 3. Edit Info ---------")
                print("------- 4. Logout ---------")
                
                auth_menu = input("Enter the action you want to perform: ")
                if auth_menu == "1":
                    receipient = input("Enter the receipient account number: ")
                    amount = input("Enter the amount you want to send: ")
                    password = input("Enter your password: ")
                    print(auth_user_action.transfer(recepient_acc_num=receipient,amount_to_send=amount,password=password))
                    
                elif auth_menu == "2":
                    print(auth_user_action.check_balance())
                
            
        elif choice == "3":
            email = input("Enter your email: ")
            print(user.view_single_user(email=email))
            
        elif choice == "4":
            print(user.view_users())
        
        elif choice == "5":
            break
        
        else:
            print("Invalid Input")
    
    