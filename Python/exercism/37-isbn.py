def is_valid(isbn):
    a = isbn.replace('-', '')
    print(list(a))
    if len(a) == 10:
        b = int(a[0]) * 10 + int(a[1]) * 9 + int(a[2]) * 8 + int(a[3]) * 7 + int(a[4]) * 6 + int(a[5]) * 5 + int(a[6]) * 4 + int(a[7]) * 3 + int(a[8]) * 2 + int(a[9]) * 1
        if b % 11 == 0:
            return True
    return False

print(is_valid("3-598-21508-8"))