def is_pangram(sentence):
    '''Determine if a sentence is a pangram'''
    sentence = set(sentence.lower())
    check = set(map(chr, range(97, 123)))
    return check.issubset(sentence)
