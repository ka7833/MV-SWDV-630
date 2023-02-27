from Hotel import Hotel
from Customer import Customer
from datetime import datetime
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Reservation(Base):
  def __init__(self, customer: Customer, hotel: Hotel, checkIn_date: datetime, checkOut_date: datetime):
    self.customer = customer
    self.checkIn_date = checkIn_date
    self.checkOut_date = checkOut_date
    self.hotel = hotel
    self.reservations = []

  __tablename__ = "Reservation"
  id = Column("id", Integer, primary_key=True)
  customer_id = Column(Integer, ForeignKey('Customer.id'))
  checkIn_date = Column(Date)
  checkOut_date = Column(Date)
  #customer = relationship("Customer",back_populates = "Reservations")

  def makeReservation(self, numOfRooms, checkIn_date, checkOut_date):
    if self.hotel.has_rooms_available():

      self.hotel.reserve_room(numOfRooms)
      self.customer.assignCustomerDates(self.checkIn_date, self.checkOut_date)

      self.booking = {} 
      self.reservationId = self.customer.lastName + str(self.customer.phoneNumber)[-4:]
      self.booking["ID"] = self.reservationId
      self.booking["FirstName"] = self.customer.firstName
      self.booking["LastName"] = self.customer.lastName
      self.booking["Email"] = self.customer.email
      self.booking["Phone"] = self.customer.phoneNumber
      self.booking["CheckInDate"] = self.customer.checkIn_date
      self.booking["CheckOutDate"] = self.customer.checkOut_date
      self.booking["NumOfRooms"] = numOfRooms
      
      self.reservations.append(self.booking)

  def viewReservation(self, id):
    reservationDetails = self.getCurrentCustomer(id)

    if(bool(reservationDetails)):
      for x in reservationDetails:
        print(f"Customer: {x['FirstName']} {x['LastName']} has booked {x['NumOfRooms']} rooms. Your check in date is {x['CheckInDate']} and check out date is {x['CheckOutDate']}")
    else:
      print("There are no reservations for ID", id)


  def cancelReservation(self, id):
    try:
      currentReservation = self.getCurrentCustomer(id)
      
      if(bool(currentReservation)):
        # remove reservation details for customer
        currentReservation.pop()
        # update the number of available rooms
        self.hotel.availableRooms += 1
        print('Reservation', id, 'Cancelled')

    except IndexError:
      print('Either the index is out of range or there is no room booking!')

  def getCurrentCustomer(self, id):
    return [reservation for reservation in self.reservations if reservation["ID"] == id]