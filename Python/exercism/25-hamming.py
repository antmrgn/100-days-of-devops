'''Calculate the Hamming Distance between two DNA strands.'''
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        # When the sequences being passed are not the same length.
        raise ValueError("Strands must be of equal length.")
    i = 0
    count = 0
    for item in strand_a:
        if strand_a[i] != strand_b[i]:
            count = count + 1
        i += 1
    return count
