def sum_of_multiples(limit, multiples):
    '''
    Given a list of factors and a limit, add up all the unique multiples of the factors that are less than the limit. 
    All inputs will be greater than or equal to zero.
    '''
    numlist = set()
    sum = 0
    for multiple in multiples:
        if multiple != 0:
            for i in range(1, limit):
                if i % multiple == 0:
                    numlist.add(i)
    for i in numlist:
        sum = sum + i
    return sum
