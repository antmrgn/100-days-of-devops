def find_anagrams(word, candidates):
    word_orig = word.lower()
    word_orig = list(word_orig)
    output = set()
    for i in candidates:
        one_word = i.lower()
        one_word = list(one_word)
        one_word.sort()
        word_orig.sort()
        if one_word == word_orig:
            output.add(i)
    output.discard(word)
    return(output)

#print(find_anagrams("solemn", ["lemons", "cherry", "melons"]))