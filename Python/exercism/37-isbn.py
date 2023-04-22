def is_valid(isbn):
    a = isbn.replace('-', '')
    print(list(a))
    sum = 0 
    k = 10
    if len(a) == 10:
        if a.isdigit():
            print("a is digit")
            for i in list(a):
#                for n in range(10, 0, -1):
                print("for range. i = " + str(i) + " k = " + str(k))
                sum = sum + int(i) * k
                k = k - 1
            if sum % 11 == 0:
                return True
        elif "X" in a[9]:
            print("elif X")
            a = list(a)
            for i, n in enumerate(a):
                if n == "X":
                    a[i] = 10
            print(a)
            print(type(a[3]))
#            if all(isinstance(e, (int)) for e in a):
            b = ''.join(str(x) for x in a)
            print(b)
            if all(ele.isdigit() for ele in b):
                print("check int")
                print(a)

                for i in a:
#                    for n in range(10, 0, -1):
                    print("for range. i = " + str(i) + " k = " + str(k))
                    sum = sum + int(i) * k
                    k = k - 1
                if sum % 11 == 0:
                    return True
                
    return False

print(is_valid("3-598-21515-X"))