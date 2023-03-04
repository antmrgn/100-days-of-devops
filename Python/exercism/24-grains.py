'''Calculate the number of grains of wheat 
on a chessboard given that the number on each square doubles.'''
def square(number):
    # how many grains were on a given square
    if number < 1 or number > 64:
        # when the square value is not in the acceptable range
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)

def total():
    # the total number of grains on the chessboard
    sum = 0
    for num in range (1, 65):
        sum = sum + 2**(num-1)
    return sum
