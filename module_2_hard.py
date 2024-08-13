import random

passs = []  # Создал пустой список
spisok2 = []  # Для удаление лишней пары
ram_dom = random.randint(3, 20)  # n = random.randint(3, 20) #    # РАНДОМ Случайное число первой вставки
rezultat = ''
print(f'Число из первой вставки {ram_dom}')  # Случайное число первой вставки
# spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] # Для удаление лишней пары
for i in range(1, ram_dom):  # Для удаление лишней пары
    spisok2.append(i)  # Для удаление лишней пары
# print(spisok2)
for ch1 in range(1, ram_dom // 2 + 1):  # Первое число пары
    for ch2 in range(2, ram_dom):  # Второе число пары
        # print(' ram_dom // 2 : ',  (ram_dom // 2))
        su_m = ch1 + ch2  # Сумма пары
        if ch1 != ch2:
            if [ch2, ch1] not in passs:
                if ram_dom % su_m == 0:  # Проверка суммы пары на деление без отстатка (на целое число)
                    # passs.append(ch1)
                    # passs.append(ch2)
                    passs.append([ch1, ch2])
                # del spisok2[ch2-1]
                # del spisok2[ch1-1]

                # ram_dom -= 2
                # i1 = str(i)
                # j1 = str(j)
                # spisok2.remove(i1)  # Удаляем элементы с указанными индексами
                # spisok2.remove(j1)  # Удаляем элементы с указанными индексами
for h in range(len(passs)):
    rezultat += str(passs[h][0]) + str(passs[h][1])
print(rezultat)
