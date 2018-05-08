import random
from prac_08.car import Car


class UnreliableCar(Car):
    reliability = random.uniform(0.0, 100.0)
    def __init__(self, name, fuel):
        super().__init__(name, fuel)


    def drive(self, distance):
        if self.reliability < distance:
            self.odometer = 0
            self.fuel = self.fuel
        else:
            super().drive(distance)



