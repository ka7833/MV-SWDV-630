class DatabaseConnection:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.connect()
        return cls.instance

    def connect(self):
        print("Connecting to the database")

def main():
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    db3 = DatabaseConnection()

    print(db1 == db2 == db3)

if __name__ == "__main__":
    main()
    
