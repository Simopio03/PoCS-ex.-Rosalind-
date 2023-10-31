#GC content Rosalind


from Bio import SeqIO
Target_seq = SeqIO.parse('rosalind_gc.txt', "fasta")
GC_content = 0
Seq_ID = ''
for element in Target_seq:
    if GC_content < (float(element.seq.count('C') + element.seq.count('G'))/len(element.seq))*100:
        GC_content = (float(element.seq.count('C') + element.seq.count('G'))/len(element.seq))*100
        Seq_ID = element.description

print(Seq_ID,GC_content)
