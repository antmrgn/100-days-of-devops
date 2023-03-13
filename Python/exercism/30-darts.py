def score(x, y):
    '''The function that returns the earned points in a single toss of a Darts game'''
    if (x ** 2 + y ** 2) ** 0.5 <= 1:
        return 10
    elif (x ** 2 + y ** 2) ** 0.5 <= 5:
        return 5
    elif (x ** 2 + y ** 2) ** 0.5 <= 10:
        return 1
    return 0
