from sqlalchemy import create_engine # somewhere to store your object
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import Hotel
from enumerations import roomType

Base = declarative_base()
class Customer(Base):
  def __init__(self, firstName, lastName, email, phoneNumber):
    self.firstName = firstName
    self.lastName = lastName
    self.email = email
    self.phoneNumber = phoneNumber
    
    self.duration = 0
    self.checkIn_date = None
    self.checkOut_date = None

  __tablename__ = "Customer"

  id = Column("id", Integer, primary_key=True)
  firstName = Column("firstName", String)
  lastName = Column("lastName", String)
  email = Column("email", String)
  phoneNumber = Column("phoneNumber", String)

  def __str__(self):
    return f"Customer: {self.firstName} {self.lastName}, Check-in: {self.checkIn_date}, Check-out: {self.checkOut_date}"

  def assignCustomerDates(self, checkIn_date, checkOut_date):
    self.checkIn_date = datetime.strptime(checkIn_date, "%Y-%m-%d")
    self.checkOut_date = datetime.strptime(checkOut_date, "%Y-%m-%d")
    
    self.duration = (self.checkOut_date - self.checkIn_date).days
    if self.duration <= 0:
      print('Check in date must be before check out date!')

  def getDuration(self):
    return self.duration

  def update_checkOut_date(self, new_date: datetime):
    self.checkOut_date = new_date

  def update_checkIn_date(self, new_date: datetime):
    self.checkIn_date = new_date


def main():
  engine = create_engine("sqlite:///myhotel.db", echo=True)
  Base.metadata.create_all(bind=engine, checkfirst=True)

  customer1 = Customer("John", "Doe", "jdoe@company.com", "888-787-2495")
  customer1.assignCustomerDates("2022-02-10", "2022-02-15")

  customer2 = Customer("Jane", "Doe", "janeDoe@company.com", "855-425-7548")
  customer2.assignCustomerDates("2022-02-12", "2022-02-20")

  customer3 = Customer("Corey", "Smith", "csmith@company.com", "768-890-1125")
  customer3.assignCustomerDates("2022-01-07", "2022-01-14")
  
  Session = sessionmaker(bind=engine)
  session = Session()
  session.add_all([customer1, customer2, customer3])
  session.commit()

  # hotel1 = Hotel.Hotel("Hotel 1", roomType.DELUXE, 10, 3)
  # amenities = ["Wifi", "Open Bar"]
  # hotel2 = Hotel.DeluxeHotel("Hotel 2", roomType.DELUXE, 20, 10, amenities)
  # hotel3 = Hotel.SuiteHotel("Hotel 3", roomType.SUITE, 100, 10, amenities, "Swimming pool")

  # session.add_all([hotel1, hotel2, hotel3])
  # session.commit()

  customerResults = session.query(Customer).all()
  print("===================All Customers=============================")

  for result in customerResults:
    print(result)
  
  print("===================Customers with last name Doe=============================")
  results = session.query(Customer).filter(Customer.lastName == "Doe")
  for result in results:
    print(result)

  print("===================Customers with email like company=============================") 
  emailResults = session.query(Customer).filter(Customer.email.like("%comp%"))
  for result in emailResults:
      print(result)

if __name__ == "__main__":
    main()
