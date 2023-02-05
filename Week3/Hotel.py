from enumerations import roomType

class Hotel:
    def __init__(self, name, roomType, totalRooms, availableRooms):
        self.name = name
        self.roomType = roomType
        self.totalRooms = totalRooms
        self.availableRooms = availableRooms
        
    def get_name(self):
        return self.name
        
    def get_price(self):
        if self.roomType == roomType.DELUXE:
            return roomType.DELUXE.value
        elif self.roomType == roomType.SUITE:
            return roomType.SUITE.value
        else:
            return roomType.LUXURY.value
        
    def has_rooms_available(self):
        if self.availableRooms > 0:
            return True
        return False
                
    def reserve_room(self, numOfRooms):
        if self.has_rooms_available():
            if numOfRooms <= self.availableRooms:
                self.availableRooms -=numOfRooms
                print(f"{numOfRooms} rooms have been reserved.")
            else:
                print(f"Cannot book {numOfRooms} rooms. There are only {self.availableRooms} rooms")
        else:
            print("There are no available rooms")
            
class DeluxeHotel(Hotel):
    def __init__(self, name, roomType, totalRooms, availableRooms, amenities = None):
        super().__init__(name, roomType, totalRooms, availableRooms)
        if amenities is None:
            self.amenities = []
        else:
            self.amenities = amenities
        
    def add_amenities(self, amenity):
        if amenity not in self.amenities:
            self.amenities.add(amenity)
        
    def show_amenities(self):
        for idx, amenity in enumerate(self.amenities, start = 1):
            print("Amenity {} = {}".format(idx, amenity))
        
class SuiteHotel(DeluxeHotel):
    def __init__(self,name, roomType, totalRooms, availableRooms, amenities, extras):
        super().__init__(name, roomType, totalRooms, availableRooms, amenities)
        self.extras = extras
    
    def show_extras(self):
        print("Extras:", self.extras)
    
    def get_available_rooms(self):
        return self.availableRooms

class LuxuryHotel(SuiteHotel):
    def __init__(self, name, roomType, totalRooms, availableRooms, amenities, extras, services = None):
        super().__init__(name, roomType, totalRooms, availableRooms, amenities, extras)
        if services is None:
            self.services = []
        else:
            self.services = services
        
        self.pointsEarned = 0
    
    def show_services(self):
        for idx, service in enumerate(self.services, start = 1):
            print("Service {} = {}".format(idx, service))
    
    def book_luxury_room(self, numOfRooms):
        if self.get_available_rooms() > 0:
            if numOfRooms <= self.availableRooms:
                self.availableRooms -=numOfRooms
                self.pointsEarned += numOfRooms
                print(f"{numOfRooms} luxury room booked!")
            else:
                print(f"Cannot book {numOfRooms} rooms. There are only {self.availableRooms} rooms")
        else:
            print("Sorry, luxury rooms not available.")
            
    def get_points_earned(self):
        return "You have earned " + str(self.pointsEarned) + " points"


hotel1 = Hotel("Hotel 1", roomType.DELUXE, 10, 3)
print(f"----------------{hotel1.get_name()}----------------")
print(hotel1.get_price())
hotel1.reserve_room(10)
hotel1.reserve_room(2)
hotel1.reserve_room(1)
hotel1.reserve_room(1) 
print(hotel1.has_rooms_available())

# Deluxe
amenities = ["Wifi", "Open Bar"]
hotel2 = DeluxeHotel("Hotel 2", roomType.DELUXE, 20, 10, amenities)
print(f"----------------{hotel2.get_name()}----------------")
print(hotel2.has_rooms_available())
hotel2.show_amenities()
print(hotel2.get_price())

# Suite
hotel3 = SuiteHotel("Hotel 3", roomType.SUITE, 100, 10, amenities, "Swimming pool")
print(f"----------------{hotel3.get_name()}----------------")
hotel3.reserve_room(2)
hotel3.reserve_room(3)
hotel3.reserve_room(4)
print(hotel3.get_available_rooms())
print(hotel3.get_price())
print(hotel3.show_extras())

hotel4 = LuxuryHotel("Hotel 4", roomType.LUXURY, 200, 100, amenities, "Swimming pool")
print(f"----------------{hotel4.get_name()}----------------")
hotel4.book_luxury_room(10)
hotel4.book_luxury_room(40)
hotel4.book_luxury_room(50)
hotel4.book_luxury_room(1) 
print(hotel4.get_price())
print(hotel4.get_available_rooms())
print(hotel4.get_points_earned())
print(hotel4.show_extras())