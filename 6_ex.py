#6th ex:

def count_unrooted_binary_trees(n):
    result = 1
    for i in range(2*n-5, 1, -2):
        result = (result * i) % 10**6
    return result
def main():
    with open('rosalind_cunr.txt') as input_data:
        n = int(input_data.read().strip())
    count = count_unrooted_binary_trees(n)
    print (count)
    with open('output.txt', 'w') as output_data:
        output_data.write(str(count))

if __name__ == '__main__':
    main()