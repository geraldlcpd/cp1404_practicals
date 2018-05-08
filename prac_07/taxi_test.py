from prac_08.taxi import Taxi

def main():
    taxi_test = Taxi('Prius 1', 100)
    taxi_test.drive(40)
    print("Fare: $", taxi_test.get_fare())
    taxi_test.start_fare()
    taxi_test.drive(100)
    print("Fare: $",taxi_test.get_fare())

main()