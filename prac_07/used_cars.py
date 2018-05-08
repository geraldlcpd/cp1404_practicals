from prac_07.car import Car

def main():
    my_car = Car(180)
    my_car.drive(30)
    print('fuel = ', my_car.fuel)
    print('odo = ', my_car.odometer)
    print(my_car)


def limo():
    limo_car = Car('Limo', 100)
    limo_car.add_fuel(20)
    print('Limo Fuel = ', limo_car.fuel)
    limo_car.drive(115)
    print('odo = ', limo_car.odometer)
    print(limo_car)

limo()