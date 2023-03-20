'''
Given a target word and a set of candidate words, 
this exercise requests the anagram set: 
the subset of the candidates that are anagrams of the target
'''
def find_anagrams(word, candidates):
    word_orig = word.lower()
    word_orig = list(word_orig)
    output = set()
    for i in candidates:
        one_word = i.lower()
        one_word = list(one_word)
        one_word.sort()
        word_orig.sort()
        if one_word == word_orig and i.lower() != word.lower():
            output.add(i)
    output.discard(word)
    return(output)

#     return set(cand for cand in candidates if word.lower() != cand.lower() and sorted(word.lower())==sorted(cand.lower()))
