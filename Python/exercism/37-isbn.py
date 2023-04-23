# verify ISBN-10 both with and without separating dashes
def is_valid(isbn):
    sum = 0 
    k = 10

# убираем дефисы
    isbnnew = isbn.replace('-', '')

# проверяем длину строки
    if len(isbnnew) == 10:
        # смотрим есть ли "X". Если есть то заменяем на 10
        if "X" in isbnnew[9]:
            isbnnew = list(isbnnew)
            isbnnew[9] = 10

        # склеиваем список в строку. Нужно для проверки элементов
        isbnstr = ''.join(str(x) for x in isbnnew)
        # проверяем что все элементы в строке являются цифрами
        if all(ele.isdigit() for ele in isbnstr):
            # виладируем ISBN-10 по формуле
            for i in isbnnew:
                sum = sum + int(i) * k
                k = k - 1
            if sum % 11 == 0:
                return True
    return False
