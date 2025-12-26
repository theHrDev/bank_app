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