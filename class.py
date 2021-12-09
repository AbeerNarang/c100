class Car(object):
    def __init__(self, model, speedlimit, color, company):
        self.model = model
        self.speedlimit = speedlimit
        self.color = color
        self.company = company
    
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")    
    
    def accelerate(self):
        print("Car accelerated")

    def brake(self):
        print("Car used brakes")

car1 = Car("EcoSport", 260, "black", "Ford")

print(car1.start())