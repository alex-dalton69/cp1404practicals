import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""line 1: 15, 20, 10. 5 is the smallest possible, 20 is the largest possible
line 2: 9, 9, 3. 3 is smallest, 10 is largest
line3: 4.377643878906982, 4.7069922184523421, 4.316918941635677. smallest is 2.5 and largest is 5.5"""