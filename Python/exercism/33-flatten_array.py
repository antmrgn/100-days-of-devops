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
                mylist.append(flatten2(i))
                print("else")
                print(i)
    return mylist

def flatten2(iterable):
    for i in iterable:
#        if i != "null" or i != "nil" or i is not None:
        if type(i) is not list:
            print("if flatten2")
            print(i)
            return i
        else:
            print("else flatten2")
            return flatten2(i)

print(flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8]))