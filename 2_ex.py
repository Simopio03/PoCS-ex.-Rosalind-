#2nd ex.






def reverse_complement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[base] for base in reversed(s))

def find_reverse_palindromes(dna):
    results = []
    for i in range(len(dna)):
        for j in range(4, 13):
            if i + j <= len(dna):
                substring = dna[i:i+j]
                if substring == reverse_complement(substring):
                    results.append((i+1, j))
    return results

def main():
    with open('rosalind_revp.txt', 'r') as file:
        data = file.read().split('\n', 1)
        dna_string = data[1].replace('\n', '')

    palindrome_positions = find_reverse_palindromes(dna_string)
    for position, length in palindrome_positions:
        print(position, length)

main()
