# from <fileName> import <className>
from CheckingAccount import CheckingAccount

def main():
    # create an instance of Checking account
    c1 = CheckingAccount("John Smith", "123 Main Street", 19371554951, 20000)
    
    # perform credit and debit operations
    c1.credit(1000)
    c1.debit(3500)
    c1.debit(5000)
    
    # show account balance
    c1.show_balance()

if __name__ == "__main__":
    main()
