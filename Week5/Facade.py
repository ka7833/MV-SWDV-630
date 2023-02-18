class ComplexLibrary:
    def operation1(self):
        print("Performing Operation 1")
        
    def operation2(self):
        print("Performing Operation 2")

class LibraryFacade:
    def __init__(self):
        self.library = ComplexLibrary()
        
    def do_operation(self):
        self.library.operation1()
        self.library.operation2()

facade = LibraryFacade()
facade.do_operation() 
