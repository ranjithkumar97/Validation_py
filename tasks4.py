class days_available:
    def __init__(self, train_id, available_days):
        self.train_id=train_id
        self.available_days=available_days

    def settrain_id(self, train_id):
        self.train_id=train_id
    def gettrain_id(self):
        return self.train_id

    def setavailable_days(self, available_days):
        self.available_days=available_days
    def getavailable_days(self):
        return self.available_days


print("enter the values from the user")
train_id = (input("enter the train_id"))
available_days = (input("enter the available_days"))  # user will enter the train_id
sc=days_available(train_id,available_days)

print("The train_id is", sc.gettrain_id())
print("The available_days is", sc.getavailable_days())
