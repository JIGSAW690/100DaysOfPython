import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Way-1
random_number = random.randint(0,len(friends)-1)
print(friends[random_number])

# Way-2
print(random.choice(friends))