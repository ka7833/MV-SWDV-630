from Customer import Customer
import datetime

class Invoice:
  def __init__(self):
    self.created = datetime.datetime.today()

  def printBill(self, customer: Customer, amountDue):
    print('---------------------------------------------')
    print("Created on:", datetime.date.today())
    print("Name: ", customer.firstName + customer.lastName)
    print("Email:", customer.email)
    print("Phone Number:", customer.phoneNumber)
    print("Check In Date:", customer.checkIn_date)
    print("Check Out Date:", customer.checkOut_date)
    print("Amount Due:", amountDue)
    print('---------------------------------------------')