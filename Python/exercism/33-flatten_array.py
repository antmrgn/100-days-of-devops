def flatten(iterable):
    mylist = []
    for i in iterable:
#        if i != "null" or i != "nil" or i is not None:
        if i != None:
            if type(i) is not list:
                print("if")
                print(i)
                mylist.append(i)
            else:
                flatten(i)
                print("else")
                print(i)
    return mylist


print(flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8]))
