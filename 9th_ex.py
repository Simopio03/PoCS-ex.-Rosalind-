#MORTAL FIBONACCI RABBITS



def rabbit_pairs(n, m):
    # Initialize a list to store pairs of rabbits for each month
    pairs = [0] * m
    pairs[0] = 1  # Initial pair of rabbits
    for i in range(1, n):
        new_pairs = sum(pairs[1:])  # New pairs of rabbits are produced by mature rabbits
        pairs[1:] = pairs[:-1]  # Move pairs to the next month
        pairs[0] = new_pairs  # Add new pairs to the first month
    return sum(pairs)


print(rabbit_pairs(6,3))

