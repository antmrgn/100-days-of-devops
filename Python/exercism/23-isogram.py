def is_isogram(string):
    d = dict(string)
    print(d)
#    print(string[1])
    for item in string:
        if string.count(item) > 1:
            return 0
        return 1

print(is_isogram('worddd'))
