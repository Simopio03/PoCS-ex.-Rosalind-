#4th_ex



def read_fasta_file(file_path):
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if not line.startswith('>'):
                sequence += line.strip()
    return sequence

def compute_failure_array(s):
    n = len(s)
    failure_array = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = failure_array[j - 1]
        if s[i] == s[j]:
            j += 1
        failure_array[i] = j
    return failure_array

# Example usage
file_path = 'rosalind_kmp.txt'
s = read_fasta_file(file_path)
failure_array = compute_failure_array(s)
print(' '.join(map(str, failure_array)))









