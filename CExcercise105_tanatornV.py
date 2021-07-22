class Vehicle:
    lcNumber = ""
    serialNumber = ""
    def AirCondition(Self):
        print("Turn on Air")

class Car(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Van(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

Car1 = Car()
Car1.AirCondition()

Pickup1 = Pickup()
Pickup1.AirCondition()

Van1 = Van()
Van1.AirCondition()

Estatecar1 = Estatecar()
Estatecar1.AirCondition()

