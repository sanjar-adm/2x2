# #Задание 1:
# import random as rd
# random_number = rd.randint(0,10)
# a = 3
# while a != 0:
#    my_number = int(input("Введите число от 0 до 10: "))
#    if my_number == random_number:
#       print('Вы угадали ')
#       break
#    else:
#       print('Вы не угадали попробуйте снова !')
#    a -= 1
#    if a == 0:
#       print('Вы проиграли! ')
#
# # 2
# while True:
#     a = int(input('введите число символа :'))
#     if a == 0:
#         break
#     print(chr(a))

# #3
# a = input('введите слово:')
# if len(a) > 10:
#     print('warning')
# elif len(a) < 10:
#     b = 10 - len(a)
#     print(a + '*' *b)

# #4
# l = []
# for i in range(6):
#     a = float(input('Введите число :'))
#     l.append(a)
# maxim = l[0]
# minim = l[1]
# for i in l:
#     if i > maxim:
#         maxim = i
#     if i < minim:
#         minim = i
# print("max:",round(maxim,2))
# print("min",round(minim,2))


# # 5
# a = int(input('enter a number: '))
# res = list(map(int, str(a)))
# maxi = max(res)
# mini = min(res)
# print(f"the maximun digit is {maxi}")
# print(f"the minimum digit is {mini}")

# # 6
# text = """
# The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
# Simple is better than complex.Complex is better than complicated.
# Flat is better than nested.Sparse is better than dense.
# Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
# Errors should never pass silently.Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one--and preferably only onUP,BROADCAST,RUNNING,MULTICASTe --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea --let's do more of those!
# """
# def get_only_capitals(s):
#     w = s.split()
#     capitals = []
#     t = s.title().split()
#     for word in w:
#         if word in t:
#             capitals.append(word)
#     return ','.join(capitals)
# print(get_only_capitals(text))


# # 7
# text = """
# The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
# Simple is better than complex.Complex is better than complicated.
# Flat is better than nested.Sparse is better than dense.
# Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
# Errors should never pass silently.Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one--and preferably only onUP,BROADCAST,RUNNING,MULTICASTe --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea --let's do more of those!
# """
# def my_func(a):
#     with open('text.txt','w')as txt:
#         txt.write(text.lower())
#
#     with open('text.txt', 'r')as txt:
#         best_list = [i for i in txt.read().split() if i.startswith('c')]
#     return best_list
# print(my_func(text))
#

# #8
# def bankomat(n):
#    moneys = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
#    d = len(str(n))
#    reversed_n = reversed(str(n))
#    count = 1
#    l = []
#    result = ''
#    for i in reversed_n:
#       wholes = int(i) * count
#       l.append(wholes)
#       count *= 10
#       count = 0
#    while n != 0:
#       if n // moneys[count] > 0:  # 12 521 yes -->2
#          a = n // moneys[count]  # 2
#          b = moneys[count]  # 5000
#          n -= a * b
#          result += a * (str(b) + " ")
#       count += 1
#    return result
#
#
# i = int(input('money: '))
# print(bankomat(i))


# #9
# def mult(a,b):
#     r = a*b
#     def inner(c,d):
#         return r + c/d
#     return inner(a,b)
# a  = int(input('Введите первое число :'))
# b = int(input('Введите второе число :'))
#
# print(mult(a,b))


# #10
# text = """
# The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.
# Simple is better than complex.Complex is better than complicated.
# Flat is better than nested.Sparse is better than dense.
# Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.
# Errors should never pass silently.Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one--and preferably only onUP,BROADCAST,RUNNING,MULTICASTe --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea --let's do more of those!
# """
# def words_with_p(text):
#    text = text.replace('\n', ' ')
#    if "p" in text:
#       return True
#    return False
# b = list(filter(words_with_p, text.split()))
# print(b)


# # 11
# dict_one = {'a':1, 'b':2, 'c':3}
# dict_two = {'d':4, 'e':5, 'f':6}
# dict_three = {'g':7, 'h':8, 'i':9}
# dict_four = {}
# t = zip(dict_one,dict_two,dict_three)
# for a,b,c in t:
#     dict_four[a] = dict_one[a]
#     dict_four[b] = dict_two[b]
#     dict_four[c] = dict_three[c]
# print(dict_four)


# # 12
# numbers = map(int,input('введите числа через пробел: ').split())
# s = int(input('сдвиг: '))
# def cesar(l,n):
#     l = list(l)
#     if n<0:
#         n = abs(n)
#         for i in range(n):
#             l = l[1:]+l[:1]
#     else:
#         for i in range(n):
#             l = l[-1:]+l[:-1]
#     return l
# print(cesar(numbers,s))

# # 13
# list_1 = [1,2,-3,4,-34,3,-3,-4,-2,-36,23,9]
# def sort_list_number(l):
#     positive_list = [i for i in l if i > 0]
#     negative_list = [i for i in l if i < 0]
#     return positive_list, negative_list
#
# print(sort_list_number(list_1))

# #14
# def which_season(m):
#     if m in (12,1,2):
#         return 'Зима'
#     elif m in (3,4,5):
#         return "Весна"
#     elif m in (6,7,8):
#         return 'Лето'
#     elif m in (9,10,11):
#         return 'Осень'
#     else:
#         return 'Нет такого месяца'
# month = int(input('month: '))
# print(which_season(month))

# # 15
# def bank(m, y):
#     first_year = m / y
#     final = 0
#     p = 0, 1
#     for i in range(y):
#         final += first_year
#         first_year += first_year * 0.1
#     return final
# m = int(input('Введите вклад :'))
# years = int(input('Введите срок :'))
# print(bank(m,years))
#
# # 16
# l = []
# while True:
#     d = int(input('weather: '))
#     if d<=-300:
#         break
#     else:
#         l.append(d)
#
# def medium_weather(l):
#     return sum(l)/len(l)
#
# print(medium_weather(l))


