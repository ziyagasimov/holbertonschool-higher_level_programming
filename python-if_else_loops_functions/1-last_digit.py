#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
    print(f"{number} and is greater than 5")
elif number == 0:
    print(f"{number} and is 0")
else :
    print(f"{number} and is less than 6 and not 0")
