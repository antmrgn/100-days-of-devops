'''Bob's responses'''
def response(hey_bob):
    hey_bob = hey_bob.strip(" ")
    if hey_bob == "" or hey_bob.isspace():
        return "Fine. Be that way!"
    elif hey_bob[-1] == '?':
        if hey_bob.isupper():
            return "Calm down, I know what I'm doing!"
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
