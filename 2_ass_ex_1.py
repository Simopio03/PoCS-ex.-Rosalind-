#1st ex.
def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        current_sequence = ''
        for line in file:
            if line.startswith('>'):
                if current_sequence:
                    sequences.append(current_sequence)
                current_sequence = ''
            else:
                current_sequence += line.strip()
        if current_sequence:
            sequences.append(current_sequence)
    return sequences

def remove_introns(dna_sequence, introns):
    for intron in introns:
        dna_sequence = dna_sequence.replace(intron, '')
    return dna_sequence

def transcribe_to_rna(dna_sequence):
    return dna_sequence.replace('T', 'U')

def translate_to_protein(rna_sequence):
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }

    protein_sequence = ''
    for i in range(0, len(rna_sequence), 3):
        codon = rna_sequence[i:i+3]
        if codon in codon_table and codon_table[codon] != 'Stop':
            protein_sequence += codon_table[codon]
    return protein_sequence

#  Usage:
if __name__ == "__main__":
    file_path = "rosalind_splc.txt"  
    sequences = read_fasta(file_path)

    # First sequence is the DNA sequence, rest are introns
    dna_sequence = sequences[0]
    introns = sequences[1:]

    
    processed_dna_sequence = remove_introns(dna_sequence, introns)
    rna_sequence = transcribe_to_rna(processed_dna_sequence)
    protein_sequence = translate_to_protein(rna_sequence)

    print("Resulting Protein Sequence:", protein_sequence)
