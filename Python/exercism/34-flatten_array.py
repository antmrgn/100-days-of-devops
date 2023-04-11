#mylist = []
def flatten(iterable):
    mylist = []
    while iterable:
        i = iterable.pop(0)
        print("while")
        print(i)
        if type(i) == list:
            print("if")
            print(i)
            iterable.extend(i)
        else:
            if i is not None:
                print("if2")
                print(i)
                mylist.append(i)
#    mylist.sort()

    return mylist


print(flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8]))
#print(flatten([1, [2, [[3]], [4, [[5]]], 6, 7], 8]))



 #   mylist = []
#     for i in iterable:
# #        if i != "null" or i != "nil" or i is not None:
#         if i != None:
#             if type(i) is not list:
#                  print("if")
#                  print(i)
#                  mylist.append(i)
#             else:
#                  flatten2(i)
#                  print("else")
#                  print(i)
#         #mylist.append(flatten2(i))
#     print("result")
#     return mylist

# def flatten2(iterable):
#     if type(iterable) is not list:
#         print("if2")
#         print(iterable)
#         return iterable
#     else:
#         print("else2")
#         print(iterable)
#         for i in iterable:
#             if type(i) is list:
#                 print("if3")
#                 print(i)
#                 flatten(i)
#             else:
#                 print("else4")
#                 print(i)
#                 return i


    # for i in iterable:
    #     print("flatten for")
    #     print(i)
    #     mylist.append(flatten2(i))
    # return mylist
#    for group in iterable:
#        for name in group:
#            mylist.append(group)
#     flatlist = sum(iterable, [])
#     return flatlist

# def flatten2(item):
#     if type(item) is not list:
#         print("flatten2 if")
#         print(item)
#         return item
#     else:
#         print("flatten2 else")
#         print(item)
#         return flatten3(item)
    
# def flatten3(item):
#     temp_list = []
#     print("flatten3")
#     print(item)
#     for i in item:
#         print("flatten3 for")
#         print(i)
#         if type(i) is not list:
#             print("flatten3 if")
#             print(i)
#             temp_list.append(i)
#         else:
#             print("flatten3 else")
#             print(i)
#             flatten3(i)    
#     return temp_list
# # 