from unreliable_car import UnreliableCar


def main():
    """Test of unreliability of cars"""
    # make cars with different reliability
    dodgy_car = UnreliableCar("Dodgy", 100, 12)
    bulletproof_car = UnreliableCar("Mint", 100, 95)

    for i in range(1, 12):
        print("Trying to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(bulletproof_car.name, bulletproof_car.drive(i)))
        print("{:12} drove {:2}km".format(dodgy_car.name, dodgy_car.drive(i)))

    print(bulletproof_car)
    print(dodgy_car)


main()
