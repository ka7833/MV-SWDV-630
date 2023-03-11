from Hotel import Hotel
from Customer import Customer
from datetime import datetime
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker
from Room import Room

Base = declarative_base()

class Reservation(Base):
  def __init__(self, customer: Customer, hotel: Hotel, checkIn_date: datetime, checkOut_date: datetime):
    self.customer = customer
    self.checkIn_date = checkIn_date
    self.checkOut_date = checkOut_date
    self.hotel = hotel
    self.reservations = []
    self.bookedFlag = False

  __tablename__ = "Reservation"
  id = Column("id", Integer, primary_key=True)
  customer_id = Column(Integer, ForeignKey('Customer.id'))
  checkIn_date = Column(Date)
  checkOut_date = Column(Date)
  #customer = relationship("Customer",back_populates = "Reservations")

  def makeReservation(self, numOfRooms, checkIn_date, checkOut_date):
    # reset booking flag
    self.bookedFlag = False
    if self.hotel.has_rooms_available():

      self.hotel.reserve_room(numOfRooms)
      self.customer.assignCustomerDates(checkIn_date, checkOut_date)
      #self.r = Room(self.hotel.roomType)

      self.booking = {} 
      self.reservationId = self.customer.lastName + str(self.customer.phoneNumber)[-4:]
      self.booking["ID"] = self.reservationId
      self.booking["FirstName"] = self.customer.firstName
      self.booking["LastName"] = self.customer.lastName
      self.booking["Email"] = self.customer.email
      self.booking["Phone"] = self.customer.phoneNumber
      self.booking["CheckInDate"] = checkIn_date
      self.booking["CheckOutDate"] = checkOut_date
      self.booking["NumOfRooms"] = numOfRooms
      
      self.reservations.append(self.booking)
      self.bookedFlag = True

    return self.bookedFlag

  def viewReservation(self, id):
    reservationDetails = self.getCurrentCustomer(id)

    if(bool(reservationDetails)):
      for x in reservationDetails:
        print(f"Customer: {x['FirstName']} {x['LastName']} has booked {x['NumOfRooms']} rooms. Your check in date is {x['CheckInDate']} and check out date is {x['CheckOutDate']}")
    else:
      print("There are no reservations for ID", id)

  def cancelReservation(self, id):
    try:
      # find the customer by id
      currentReservation = self.getCurrentCustomer(id)
      # [{'ID': 1, 'Name': 'John', 'Email': 'john@company.com'}]
      if(bool(currentReservation)):
        # remove reservation details for customer
        self.reservations = [reservation for reservation in self.reservations if not reservation["ID"] == id]

        # update the number of available rooms
        self.hotel.availableRooms += 1
        print('Reservation', id, 'Cancelled')
      else:
        print("No reservation found for id", id)

    except IndexError:
      print('Either the index is out of range or there is no room booking!')

  def getCurrentCustomer(self, id):
    return [reservation for reservation in self.reservations if reservation["ID"] == id]

  def modifyReservation(self, id, numOfRooms, newCheckInDate, newCheckOutDate):
    currentReservation = self.getCurrentCustomer(id)
    if(bool(currentReservation)):
      self.cancelReservation(id)
      bookedFlag = self.makeReservation(numOfRooms, newCheckInDate, newCheckOutDate)
      
      if not bookedFlag:
        # Fallback - reserve with old dates
        print("Modification unsuccessful. Reserving with initial dates")
        self.makeReservation(currentReservation[0]["NumOfRooms"],self.checkIn_date, self.checkOut_date)

    else:
      print("Invalid ID")



