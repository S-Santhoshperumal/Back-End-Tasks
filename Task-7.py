class Bank_Account:
    def __init__(self):
        self.Name=""
        self.Amount=0
        self.Address=""
        self.AccountNo=0
        self.withdraw_amount=0
        self.deposit=0
       
    
    def CreateAccount(self):
        self.Name=input('Enter the Account Holder Name:')
        self.Amount=int(input('Enter the Amount:'))
        self.Address=input('Enter the Address:')
        self.AccountNo=int(input('Enter the Account Number:'))
        self.withdraw_amount=int(input('Enter the Withdraw Amount:'))
        self.deposit=int(input('Enter the deposit amount:'))

    def DisplayInformation(self):
        print('--------Your Account Information----------')
        print('Name of the Acount Holder:',self.Name)
        print('Address:',self.Address)
        print(' Account Number:',self.AccountNo)
        print('Current Balance:',self.Amount)
        print('Withdraw amount:',self.withdraw_amount)
        print('Deposit amount:',self.deposit)
        
        
    def Deposit(self):
        self.Amount += self.deposit
        print(f'Deposited {self.deposit}. New balance is {self.Amount}')
        
        
    def withdraw(self):
        if self.withdraw_amount > self.Amount:
            print("Insufficient funds")
        else:
            self.Amount -= self.withdraw_amount
            print(f'Withdraw {self.withdraw_amount}. New balance is {self.Amount}')
            
            
    def check_balance(self):
        print(f'Current Balance: {self.Amount}')
           
def main():
    User_1=Bank_Account()
    print('----------------Creating First Account------------')

    User_1.CreateAccount()
    User_1.DisplayInformation()
    User_1.withdraw()
    User_1.Deposit()
    User_1.check_balance()
    print()

    User_2=Bank_Account()
    print("Creating Second Account:")

    User_2.CreateAccount()
    User_2.DisplayInformation() 
    User_2.withdraw()
    User_2.Deposit()
    User_2.check_balance()
    
    
    
    
    
if __name__=='__main__':
    main()

