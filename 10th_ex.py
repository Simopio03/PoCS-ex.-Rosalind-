#inferring mRna from protein
# Dictionary mapping amino acids to the number of corresponding RNA codons



amino_acid_codons = {
    'F': 2, 'L': 6, 'I': 3, 'M': 1, 'V': 4, 'S': 6, 'P': 4, 'T': 4, 'A': 4,
    'Y': 2, 'H': 2, 'Q': 2, 'N': 2, 'K': 2, 'D': 2, 'E': 2, 'C': 2, 'W': 1, 'R': 6, 'G': 4,
    'Stop': 3  # Stop codon
}

def total_rna_strings(protein_sequence):
    total_codons = 1
    for aminoacid in protein_sequence:
        total_codons = (total_codons * amino_acid_codons[aminoacid]) % 1000000
    return (total_codons * amino_acid_codons['Stop']) % 1000000

print(total_rna_strings("MYPCAQDARAIHVCLGSIMGQWFCYHKWADQAWDIVNFWWSMICKYVPTDWRWLRMGCCMTELNEPTDSAWECWSHQVYRTGVKVMYWYVLQCRIDACFNLNRWMGVNWYPMDCVADTTHSWPHYERTMRWTFLNELYDPYSEEMSEPIQPHTDWICKCLYNSTPWIQCFIHVVISFCCCEVCDPKVKFMCHVEQIVDTWCYYGKCYLENKDYWFAQYTTKDSSQAECFMIARLLDFWSQIHNVTAEVSTVLFNFPCRGGMYSHARNISIKWDCCMEQNKGHKWMTAYPSWKALLLWTCDQDKEFYALFQAMAPTDIVTRTEAQKPWWWSWMSFSIMLSSMHHVINDQEPVSEVIYAFYNMEYNKDNPNVKWQHTGKFAMDFLGNERKKSYVVNPAGECFVTWMFELSQPEPMVDQKMGLPINGNFRLNCAPESLIPDPAVGAIITVFAAMWISEEVVFGHDKSQEVSLVWSQCWVNARLLCINIVYECVDKNYYHCQLIILTVCRKPPWCVLKMFVCAFGAFLAFCHCEESMADIRFHMASQMAFRPANYETIDPSGKVADSGLSLFRKEWLWYGNQEDNFIEHNFTVMPVDILEIMILWHDSSEQLEHIPHSYELCHMGYLRPLKGIFWEPEWNVMTFLPVDACMHWQAWIGATEYVEWACQEEWGLQNHCLYPDWVDTPHETEMILELLRKKNLEAWMWWSKGVEIHKETLQEHWLPANNFVCFVAKINKCPQTQCHRNHDYVGIHFKWKTLHWFKMVYNWIWYLIPAPGFCTFIRLEYLMVMWHLNVFWCTTLFYAHQTIAGKGYGLHRIDIAGPLDPEQKWSWEQIWHLDDRQYIPLPADNMVTEWLPFCMYNMICWQWCANVTNRHWTMFFQGEVPRHCTYFNEPHHIMMYKMPRNLNAKVLIIAITFYLLYFPQVLMFGEFDNVKWYKLRRMHSDHNKDKPDENSFHMSWPDEALFGCWCMCKIDAWGRNLWNRFSGWQHERIMNQSVMYW"))
