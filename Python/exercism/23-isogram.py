def is_isogram(string):
    word = list(string.lower())
    for item in word:
        if item.isalpha(): 
            if word.count(item) > 1:
                return False
    return True
