import random as rn
from datetime import datetime

# Import the random function and generate both a random number between 0 and 1 as well as a random number between 1 and 10.
randomnumber_0_1 = rn.random()

randomnumber_1_10 = rn.randint(1, 10)

# Use the datetime library together with the random number to generate a random, unique value.
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

random_part = rn.randint(1000, 9999)

unique_value = f"{timestamp}_{random_part}"

print(randomnumber_0_1)
print(randomnumber_1_10)
print(unique_value)
