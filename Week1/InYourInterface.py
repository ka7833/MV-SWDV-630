class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)

  def __contains__(self, item):
      return item in self.__myTeam
    
  def __iter__(self):
      return iter(self.__myTeam)  

def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  print (len(classmates))
  print("Tim" in classmates)
  print("Sam" in classmates)
  iterator = iter(classmates)
  
  for c in iterator:
      print(c)
      
main()