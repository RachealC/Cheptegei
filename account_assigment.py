# class Bank_Account:
#     def __init__(self):
#         self.balance=0
#         print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
#     def deposit(self):
#         amount=float(input("Enter amount to be Deposited: "))
#         self.balance += amount
#         print("\n Amount Deposited:",amount)
 
#     def withdraw(self):
#         amount = float(input("Enter amount to be Withdrawn: "))
#         if self.balance>=amount:
#             self.balance-=amount
#             print("\n You Withdrew:", amount)
#         else:
#             print("\n Insufficient balance  ")
 
#     def display(self):
#         print("\n Net Available Balance=",self.balance)
 
# # Driver code
  
# # creating an object of class
# s = Bank_Account()
  
# # Calling functions with that class object
# s.deposit()
# s.withdraw()
# s.display()

class BankAccount:
    # create the constuctor with parameters: accountNumber, name and balance 
    def __init__(self,accountNumber, name, balance):
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
        
    # create Deposit() method
    def Deposit(self , d ):
        self.balance = self.balance + d
    
    # create Withdrawal method
    def Withdrawal(self , w):
        if(self.balance < w):
            print("impossible operation! Insufficient balance !")
        else:
            self.balance = self.balance - w
    # create bankFees() method
    def bankFees(self):
        self.balance = (95/100)*self.balance
        
    # create display() method
    def display(self):
        print("Account Number : " , self.accountNumber)
        print("Account Name : " , self.name)
        print("Account Balance : " , self.balance , " KES")
        
newAccount = BankAccount(2178514584, "Racheal Cheptegei" , 2700)
# Creating Withdrawal Test
newAccount.Withdrawal(300)
# Create deposit test
newAccount.Deposit(200)
# Display account informations
newAccount.display()