class route:
    def __init__(self, train_id, stop_number,station_id,arrival_time):
        self.train_id=train_id
        self.stop_number=stop_number
        self.station_id=station_id
        self.arrival_time=arrival_time

    def settrain_id(self, train_id):
        self.train_id=train_id
    def gettrain_id(self):
        return self.train_id

    def setstop_number(self, stop_number):
        self.stop_number=stop_number
    def getstop_number(self):
        return self.stop_number

    def setstation_id(self, station_id):
        self.station_id =station_id

    def getstation_id(self):
        return self.station_id

    def setarrival_time(self, stop_number):
        self.arrival_time = arrival_time

    def getarrival_time(self):
        return self.arrival_time

print("enter the values from the user")
train_id = (input("enter the train_id"))
stop_number = (input("enter the stop_number"))  # user will enter the stop_number
station_id = ("enter thestation_id")  # user will enter the station_id
arrival_time= input("enter the arrival_time")


sc=route(train_id,stop_number,station_id,arrival_time)

print("The train_id is", sc.gettrain_id())
print("The stop_number is", sc.getstop_number())
print("the station_id ", sc.getstation_id())
print("the arrival time is " ,sc.getarrival_time() )
