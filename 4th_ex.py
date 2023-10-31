#4th ex

def rabbit_pairs(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        # Initialize a list to store the number of rabbit pairs for each month
        pairs = [0] * n
        pairs[0], pairs[1] = 1, 1  # First two months have 1 pair each

        # Calculate the number of rabbit pairs for the remaining months using the recurrence relation
        for i in range(2, n):
            pairs[i] = pairs[i - 1] + k * pairs[i - 2]

        return pairs[-1]  # Return the number of rabbit pairs after n months

# Example usage
if __name__ == "__main__":
    n = 5
    k = 3

    if 1 <= n <= 40 and 1 <= k <= 5:
        total_pairs = rabbit_pairs(n, k)
        print("Total number of rabbit pairs after", n, "months:", total_pairs)
    else:
        print(" Ensure that n is between 1 and 40, and k is between 1 and 5.")
