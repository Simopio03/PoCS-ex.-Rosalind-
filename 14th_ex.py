from collections import Counter

def read_fasta(file_path):
    with open(file_path, 'r') as file:
        sequences = [line.strip() for line in file if not line.startswith(">")]
    return sequences

def create_profile_matrix(dna_strings):
    nucleotides = "ACGT"
    profile_matrix = [[Counter(column)[n] for n in nucleotides] for column in zip(*dna_strings)]
    return profile_matrix

def find_consensus_string(profile_matrix):
    nucleotides = "ACGT"
    consensus_string = ''.join(nucleotides[max(range(4), key=lambda i: counts[i])] for counts in profile_matrix)
    return consensus_string

# Example usage
if __name__ == "__main__":
    file_path = "rosalind_cons.txt"  
    dna_strings = read_fasta(file_path)
    profile_matrix = create_profile_matrix(dna_strings)
    consensus_string = find_consensus_string(profile_matrix)

    
    print("Consensus String:", consensus_string)
    print("Profile Matrix:")
    for nucleotide, counts in zip("ACGT", zip(*profile_matrix)):
        print(f"{nucleotide}: {' '.join(map(str, counts))}")