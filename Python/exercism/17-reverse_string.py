def reverse(text):
    '''Reverse a string'''
    k = 0
    new_text = ''
    for i in text:
        k -= 1
        new_text = new_text + (text[k])
    return new_text
