from prac_08.SilverServiceTaxi import SilverServiceTaxi

def main():
    silver_taxi = SilverServiceTaxi('Mercedes', 80, 3)
    silver_taxi.drive(50)
    print(silver_taxi.get_fare())
    print(silver_taxi.__str__())
main()