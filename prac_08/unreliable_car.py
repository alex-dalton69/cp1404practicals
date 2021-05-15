from random import randint
from car import Car


class UnreliableCar(Car):
    """A car that is unreliable to drive"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """generate random number for probability that car wont start"""
        random_num = randint(1, 100)
        if random_num >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
