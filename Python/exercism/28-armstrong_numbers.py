'''some code to determine whether a number is an Armstrong number'''
def is_armstrong_number(number):
    sum = 0
    for i in str(number):
        sum = sum + int(i) ** len(str(number))
    if sum == number:
        return True
    return False
