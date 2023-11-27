#16th_ex


#CONSENSUS AND PROFILE


from collections import Counter

def read_fasta_file(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences

def consensus_string_and_profile(dna_strings):
    n = len(dna_strings[0])
    profile = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}

    for dna in dna_strings:
        for i, nucleotide in enumerate(dna):
            profile[nucleotide][i] += 1

    consensus = ''
    for i in range(n):
        max_count = 0
        max_nucleotide = ''
        for nucleotide, counts in profile.items():
            if counts[i] > max_count:
                max_count = counts[i]
                max_nucleotide = nucleotide
        consensus += max_nucleotide

    return consensus, profile

# Usage
file_path = 'rosalind_cons.txt'
dna_strings = read_fasta_file(file_path)
consensus, profile = consensus_string_and_profile(dna_strings)
print(consensus)
for nucleotide, counts in profile.items():
    print(f"{nucleotide}: {' '.join(map(str, counts))}")
