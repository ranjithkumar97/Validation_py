class train:
    def __init__(self, train_id , train_name , train_type , source_station , destination_station , source_id , destination_id):
        self.train_id = train_id
        self.train_name = train_name
        self.train_type = train_type
        self.source_station = source_station
        self.destination_station = destination_station
        self.source_id = source_id
        self.destination_id = destination_id

    def settrain_id(self,train_id):
        self.train_id = train_id
    def gettrain_id(self):
        return self.train_id
    def settrain_name(self,train_name):
        self.train_name = train_name
    def gettrain_name(self):
        return self.train_name
    def settrain_type(self,train_type):
        self.train_type = train_type
    def gettrain_type(self):
        return self.train_type

    def source_station(self, source_station):
        self.source_station = source_station

    def getsource_station(self):
        return self.source_station

    def setdestination_station(self, destination_station):
        self.destination_station = destination_station

    def getdestination_station(self):
        return self.destination_station

    def setsource_id(self, source_id):
        self.train_type = source_id

    def getsource_id(self):
        return self.source_id

    def setdestination_id(self, destination_id):
        self.destination_id = destination_id

    def getdestination_id(self):
        return self.destination_id
print("enter the values you want")
train_id = int(input("enter the train_id"))
train_name = (input("enter the train_name"))
train_type = (input("enter the train_type"))

source_station = str(input("enter the source_station"))
destination_station = str(input("enter the destination_station"))
source_id = int(input("enter the source_id"))
destination_id = int(input("enter the destination_id"))

tr = train(train_id, train_name, train_type, source_station, destination_station, source_id, destination_id )
print("train_id is", tr.gettrain_id())
print("train_name is", tr.gettrain_name())
print("train_type is", tr.gettrain_type())

print("source_station is", tr.getsource_station())
print("destination_station is", tr.getdestination_station())
print("source_id is", tr.getsource_id())
print("destination_id is", tr.getdestination_id())












