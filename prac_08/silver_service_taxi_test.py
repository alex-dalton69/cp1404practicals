from silver_service_taxi import SilverServiceTaxi


def main():
    fancy_taxi = SilverServiceTaxi("Fancy taxi test drive", 100, 2)
    fancy_taxi.drive(18)
    print(fancy_taxi)
    print("The fancy taxi cost: ${:.2f}".format(fancy_taxi.get_fare()))


main()
