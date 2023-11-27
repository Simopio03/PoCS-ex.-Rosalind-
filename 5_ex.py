from Bio import Phylo

def generate_character_table_from_file(file_path):
    tree = Phylo.read(file_path, "newick")
    taxa = sorted(tree.get_terminals(), key=lambda x: x.name)
    table = []

    for clade in tree.get_nonterminals(order='preorder'):
        # Skip the root
        if clade == tree.root:
            continue
        row = ['0'] * len(taxa)
        for terminal in clade.get_terminals():
            row[taxa.index(terminal)] = '1'
        table.append(''.join(row))

    return table

file_path = "rosalind_ctbl.txt"
table = generate_character_table_from_file(file_path)

for row in table:
    print(row)
