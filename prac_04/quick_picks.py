import random

NUM_IN_LINE = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    number_of_picks = int(input("How many quick pics? "))
    while number_of_picks < 0:
        print("Invalid number of picks!")
        number_of_picks = int(input("How many quick pics? "))
    for i in range(0, number_of_picks):
        quick_pick = []
        for j in range(NUM_IN_LINE):
            random_num = random.randint(MINIMUM, MAXIMUM)
            while random_num in quick_pick:
                random_num = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(random_num)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
