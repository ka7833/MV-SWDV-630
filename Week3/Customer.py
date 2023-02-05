from datetime import date

class Customer:
    def __init__(self, fname, lname, numOfGuests):
        self.fname = fname
        self.lname = lname
        self.numOfGuests = numOfGuests
        
    def assignCustomerDates(self, chkInDate, chkOutDate):
        self.chkInDate = date(chkInDate[0], chkInDate[1], chkInDate[2])
        self.chkOutDate = date(chkOutDate[0], chkOutDate[1], chkOutDate[2])
        self.duration = (self.chkOutDate - self.chkInDate).days
        if self.duration <= 0:
            print('Check in date must be before check out date!')