class Reminder:

    def __init__(self, file):
        self.file = file
        self.data = []
        f = open(file,"w+")
        self.data = list(f.readlines())

        pass
    def add(self, time, message):
        self.data.append([time, message])
        pass
    def update(self, id, time, message):
        pass
    def delete(self, id):
        pass
    def getReminderToday(self):
        pass
    
    
    def printAll(self):
        print(self.data)
       
def run():
        reminder = Reminder("reminder.txt")
        userTime = str(input("Enter time to be reminded : "))
        userMessage = str(input("Enter message to be reminded : "))
        print(userTime,userMessage)
        reminder.add(userTime,userMessage)
        reminder.printAll()
        print("payalpayal")



if __name__ =="__main__":
    run()