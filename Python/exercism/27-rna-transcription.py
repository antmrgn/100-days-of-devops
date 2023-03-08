# Given a DNA strand, return its RNA complement (per RNA transcription).
def to_rna(dna_strand):
    s = list(dna_strand)
    i = 0
    for item in s:
        if s[i] == "G":
            s[i] = "C"
        elif s[i] == "C":
            s[i] = "G"
        elif s[i] == "T":
            s[i] = "A"
        elif s[i] == "A":
            s[i] = "U"
        i += 1
    return "".join(s)



# # Use translate with maketrans to return the value.
# LOOKUP = str.maketrans("GCTA", "CGAU")

# def to_rna(dna_strand):
#     return dna_strand.translate(LOOKUP)
