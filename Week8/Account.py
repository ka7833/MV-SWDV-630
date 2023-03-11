from AccountStatus import *

class Account:
  def __init__(self, userName, password, status = AccountStatus.ACTIVE):
    self.userName = userName
    self.password = password
    self.status = status

  def resetPassword(self, newPassword):
    self.password = newPassword

  def getUserName(self):
    return self.userName

  def getPassword(self):
    return self.password