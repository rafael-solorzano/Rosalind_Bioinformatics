# Goal: return the reverse complement of a given DNA string
# e.g., the reverse complement of "GTCA" is "TGAC"

s = "GTACTGAACACACACCGCATACCTTCCTCCTCTTTCAGTGTAATAGCTGATAATCTCGCTCGGGAACGGCAGTCGAGCGCTCTCCTCGACTTCTCGTCACCCATGGTCCGGCAGCGCCAGAACCGTGTGTTATCAGATCACTATATTGATGCTTTGGCCGTAATTGAGCTACTGAATCACACCGGCGTCCTCTGAGGTAAGTACGCTGGGGGGTTTCAGCGGGGTAAAAAATTCGCTTTACGTCGCGAACCAAACCGTGGAGGAACAAGTCGACGTCTGGCACCTGCTGTCCGACCATCTCCTCATGTGCCAAATCACCGTTGAACAAGTCCGGGGAGCGTTAGCGATGACAACTGTCATATTTTTCCTGAAATGTTTTATCTCCCATGCAGAGATCCGGCGAACGCTGCAACAGCAATTTCTCTGCACAAGTCCTCCGTAAGGTATCCCCGGTGAGTGACAAAAGCCTGGTAGAAGGTCTCTACATTTGTGCACTATAAATGATGCTAATTCATCACCCTATTAGTCTTTCGGAGAACCTAACGCGACGTAAGTACCGGCGTACCCACGGCCGCTTAAGAGTATACCAATTCACCACCTTGCAGAAAAAGAGTCATCGTATAAGGACACCCGAAAGTCGAATTCCTACAAAATCATCTAATTGTCCCATGCTGGATTGCTTCCGAAAACCTCCTACGCATTGAATACGGCTTGTGATTAGTTCACAGTCTTTCTTTTATGGCGTTCACAACGTGGTTCTGAAAAGCAACCCGACCCATATTCCCGGGCGACAACAAATGTTGTGGCTACGAAGCATATGTCATATACGTTATCTTTACGACAAACCTTGCCGAGGACCGATCAAGCTACAATACTGCACGCTAGATATTATAATTAGCTTCTCCCAGATTACCGCACGCGGCC" #DNA string

s_c = "" #storage for complement


#step 1: find complement
for x in s:
    if x == "A":
        s_c += "T"
    elif x == "T":
        s_c += "A"
    elif x == "C":
        s_c += "G"
    else:
        s_c += "C"


#step 2: reverse the string
print(s_c[::-1])

