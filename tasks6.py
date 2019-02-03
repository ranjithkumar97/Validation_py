class station:
    def __init__(self, station_id, station_name):
        self.station_id=station_id
        self.station_name=station_name

    def setstation_id(self, station_id):
        self.station_id=station_id
    def getstation_id(self):
        return self.station_id

    def setstation_name(self, station_name):
        self.station_name=station_name
    def getstation_name(self):
        return self.station_name


print("enter the values from the user")
station_id = (input("enter the station_id"))
station_name = (input("enter the station_name"))  # user will enter the station_id
sc=station(station_id,station_name)

print("The train_id is", sc.getstation_id())
print("The available_days is", sc.getstation_name())
