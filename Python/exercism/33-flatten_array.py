mylist = []
def flatten(iterable):
 #   mylist = []
    for i in iterable:
#        if i != "null" or i != "nil" or i is not None:
        if i != None:
            if type(i) is not list:
                print("if")
                print(i)
                mylist.append(i)
            else:
                flatten2(i)
                print("else")
                print(i)
    print("result")
    return mylist

def flatten2(iterable):
    if type(iterable) is not list:
        print("if2")
        print(iterable)
        return iterable
    else:
        print("else2")
        print(iterable)
        flatten(iterable)


print(flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8]))
#print(flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8]))