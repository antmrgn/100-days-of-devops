def convert(number):
    '''to convert a number into a string that contains raindrop sounds corresponding to certain potential factors'''
    a = ""
    if number % 3 == 0:
        a = "Pling"
    if number % 5 == 0:
        a = a + "Plang"
    if number % 7 == 0:
        a = a + "Plong"
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
    return a


# def convert(number):
#     return (("" if number % 3 else "Pling") +
#             ("" if number % 5 else "Plang") +
#             ("" if number % 7 else "Plong")) or str(number)
