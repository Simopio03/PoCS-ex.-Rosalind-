#3rd_ex




import itertools

def generate_strings(alphabet, n):
    alphabet = sorted(alphabet)
    strings = [''.join(x) for x in itertools.product(alphabet, repeat=n)]
    strings.sort()
    return strings

def main():
    alphabet = ['A', 'B', 'C', 'D','E','F']  # Replace with the given alphabet
    n = 3  # Replace with the given value of n
    result = generate_strings(alphabet, n)
    for string in result:
        print(string)

main()
