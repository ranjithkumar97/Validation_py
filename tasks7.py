class train_status:
    def __init__(self, train_id, available_date,booked_seats,waiting_seats):
        self.train_id=train_id
        self.available_date=available_date
        self.booked_seats=booked_seats
        self.waiting_seats=waiting_seats

    def settrain_id(self, train_id):
        self.train_id=train_id
    def gettrain_id(self):
        return self.train_id

    def setavailable_date(self, available_date):
        self.available_date=available_date
    def getavailable_date(self):
        return self.available_date

    def setbooked_seats(self, bookes_seats):
        self.booked_seats=booked_seats
    def getbookes_seats(self):
        return self.booked_seats


    def setwaiting_seats(self, bookes_seats):
        self.waiting_seats=waiting_seats
    def getwaiting_seats(self):
        return self.waiting_seats



print("enter the values from the user")
train_id = input("enter the train_id")
available_date = input("enter the available_date")  # user will enter the train_id
booked_seats=input("enter the booked_seats")
waiting_seats=input("enter the waiting_seats")
sc=train_status(train_id,available_date,booked_seats,waiting_seats)

print("The train_id is", sc.gettrain_id())
print("The available_days is", sc.getavailable_date())
print("the booked seats is" ,sc.getbookes_seats())
print("the waiting seats is" ,sc.getwaiting_seats())
