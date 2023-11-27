def generate_unrooted_trees(current_tree, new_taxa):
    new_trees = []
    for i in range(1, len(current_tree) - 2):
        j = -1
        if current_tree[i] not in '(),;':
            j = i
        if current_tree[i] == '(':
            m = 1
            for j in range(i + 1, len(current_tree)):
                if current_tree[j] == '(':
                    m += 1
                elif current_tree[j] == ')':
                    m -= 1
                if m == 0:
                    break
        if j != -1:
            new_tree = current_tree[:i] + ['('] + current_tree[i:j + 1] + [','] + [new_taxa] + [')'] + current_tree[j + 1:]
            new_trees.append(new_tree)
    return new_trees

def main():
    with open('rosalind_eubt.txt', 'r') as file:
        taxa = file.read().split()
        initial_tree = ['(', '(', taxa[1], ',', taxa[2], ')', ')', taxa[0], ';']
    
    new_taxa_list = taxa[3:]
    current_trees = [initial_tree]

    for new_taxa in new_taxa_list:
        updated_trees = []
        for tree in current_trees:
            updated_trees.extend(generate_unrooted_trees(tree, new_taxa))
        current_trees = updated_trees[:]

    for tree in current_trees:
        print(''.join(tree))

if __name__ == "__main__":
    main()



