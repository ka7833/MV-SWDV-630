from ReservationStatus import ReservationStatus
from RoomType import RoomType

class Room():
  # class variables
  reservedStatus = {}
  # Available Room
  reservedStatus["1"] = ReservationStatus.AVAILABLE
  # Reserved Room
  reservedStatus["2"] = ReservationStatus.RESERVED

  def __init__(self, suite):
    self.suiteType = suite
    self.status = Room.reservedStatus["1"]

    if self.suiteType == RoomType.DELUXE:
      self.price = 100
    elif self.suiteType == RoomType.SUITE:
      self.price = 200
    elif self.suiteType == RoomType.LUXURY:
      self.price = 300

  def returnRoomPrice(self):
    return self.price