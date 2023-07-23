#DNA to RNA: all instances of 'T' become 'U'

DNA = ""
RNA = "" #storage var for transcribed RNA

for x in DNA:
    if x == "T":
        RNA += "U"
    else:
        RNA += x

print(RNA)
