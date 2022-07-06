'''
Bank System using OOP

Parent Class : User
Holds details about an user
Has a function to show user details

Chil Class : Bank
Stores details about the account balance
Stores details about the amount
Allows for deposits,withdraw,view_balance
'''
class User():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    def show_user_details(self):
        print("User's Details")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ",self.gender)

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender) # super() -> write the selfs arguements for is
        self.balance = 0
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Account balance has been updated : ₹",self.balance)
    def withdraw(self,amount):
        self.amount = amount
        if(self.amount > self.balance):
            print("Insufficent Balance | Balance Available : ₹", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : ₹", self.balance)

    def view_balance(self):
        self.show_user_details()
        print("Account balance : ₹", self.balance)
