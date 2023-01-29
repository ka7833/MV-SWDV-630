class CheckingAccount:
    def __init__(self, name, address, accountNumber, balance):
        self.__name = name
        self.__address = address
        self.__accountNumber = accountNumber
        self.__balance = balance
     
    def credit(self, amount):
        self.__balance += amount
        
    def debit(self, amount):
        if self.__balance < amount:
            print("Insufficient funds for account " + str(self.accountNumber))
        else:
            self.__balance -= amount
            
    def show_balance(self):
        print(f"The account balance on account {self.__accountNumber} for {self.__name} is {self.__balance}")