from prac_08.taxi import Taxi

class SilverServiceTaxi(Taxi):

    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fare_distance = 0
        self.price_per_km = Taxi.price_per_km * fanciness

    def drive(self, distance):
        super().drive(distance)

    def get_fare(self):
        return super().get_fare() + SilverServiceTaxi.flag_fall

    def __str__(self):
        super().__str__()