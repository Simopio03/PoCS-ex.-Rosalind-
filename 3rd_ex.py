#3rd ex
dict_conversion = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
new_s = ''

sequence='AAAACCCGGT'

for pos in range(len(sequence) - 1, -1, -1):
    new_s += dict_conversion[sequence[pos]]
print(new_s)