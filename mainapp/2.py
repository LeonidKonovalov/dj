# print(input('How r u?'))
# print(input('Введите:'))
# n=input()
# print(type(int(n)))
# 1 2 3
# 5
# 1
# 2
# 3
# 4
# 5
# m='1 2 3' - > a,b,c=1,2,3
# n=input()
# for n in range(1,)

# m='1 2 3'
# for i in m:
#   print(i)
# print(m.split(' '))
# l=m.split(' ')
# print(type(m[0]))
# for i in l:
#   print(int(i)*2)

# Количество чисел 3 - > input()
# сами числа 1
# 2
# 3
# a=[]
# for i in range(int(input())):
#   a.append(int(input()))
# print(a)

# 2
# 3
# 4
# . 0

# lst=[int(i) for i in iter(input, '.')]
# # print(lst)
# lst=[]
# n=input()
# while n!='.':
#   lst.append(int(n))
#   n=input()
# print(lst)

# mylist=[1,2,3,4,5]

# for i in range(0,5): # [0,5) 0,1,2,3,4
#   print(mylist[i], i)

# a=10 # 20
# b=20 # 10
# if a<b: # от 10 до 20 - от а до б
#   for i in range(a,b):
#     if i%2==0:
#       print(i)
#   # print(*(i for i in range(a,b) if i%2==0))
# else: # от 10 до 20 - от б до а
#   for i in range(b,a):
#     if i%2==0:
#       print(i)

# a=int(input())
# b=int(input())
# s=0
# if a<b:
#   for i in range(a,b):
#     s+=i
# elif b<a:
#   for i in range(b,a):
#     s+=i
# print(s)

# s=0
# if a>b:
#   temp=a
#   b=a
#   a=temp

#   # a,b=b,a
# for i in range(a,b):
#     s+=i
# print(s)
# print(sum(range(a,b)))
# print(sum([10,11,12,13,14,15,16,17,18,19]))
# Домашняя работа
# 1.
# money=500 #input
# cost=1300
# if money>cost:
#   print ('Покупает')
# else:
#   print('Не покупает')
# print('Покупает' if money>cost else 'Не покупает')

# 2
# n=1#

# if in n ['красный']:
#   print('красный')
# else:
#   print('голубой')
# print(rainbow_color[3])
# for i in rainbow_color:
#   print(i)
# 3
'''Напишите программу,
которая принимает на вход натуральное число n и печатает первые n цветов радуги с большой буквы.
При этом, если n > 7, программа должна ответить "."Радуга состоит только из семи цветов'''
# n=int(input())
# rainbow_color = ['розовый', 'фиолетовый', 'голубой', 'красный', 'белый', 'зеленый', 'синий']
# if not n>7:
#   for i in range(n):  #0-4 5 раз
#    print((rainbow_color[i]))
# else:
#   print("Радуга состоит 'только' из семи цветов")

# n=int(input())
# rainbow_color = ['розовый', 'фиолетовый', 'голубой', 'красный', 'белый', 'зеленый', 'синий']
# if not n>7:
#   for i in range(n):  #0-4 5 раз
#    print((rainbow_color[i]))
# else:
#   for i in range(7):
#     print((rainbow_color[i]))
#   print("Радуга состоит 'только' из семи цветов")
# 4
# 7
# 5
# 3
# 0 . -1 стоп выход
# l=[]
# n=int(input())
# while n!=0:
#   l.append(n)
#   print(l)
#   n=int(input())
# sum=0
# for i in l:
#   sum+=i
# print(sum)

# sum=0
# n=int(input())
# while n!=0:
#   sum+=n
#   print('sum=',sum)
#   n=int(input())
# print(sum)

# money = int(input('введите сумму денег'))
# goods_count = int(input('количество товаров'))
# 2000
# 4 товара
# 1000 осталось 1000
# 100 осталось 900
# 500 осталось 400
# 500 не может купить

# prices=[]
# for i in range(goods_count):
#   prices.append(int(input('Введите цену')))
# print(prices)

# sum=0
# i=0
# while money>sum:
#   sum+=prices[i]
#   i+=0
# print('денег хватило на', sum-prices[i])

# print(f'{money} хватило на {goods_count} товаров, {prices}')
# if money>sum(prices):
#   print ('Покупает')
# else:
#   print('Не покупает')
# print('Покупает' if money>cost else 'Не покупает')
# sum=0
# sum+=int(input('Введите цену'))

# cash = int(input())
# n = 0
# while n <= cash:
#     a = int(input())
#     n += a
# print("Стоп, Джон!")
# print(n - a)

# калькулятор
# високосный год

# 1 2 +
# a,b,c = input().split()
# print(a,c,b)

# 1
# 2
# +
# a=int(input())
# b=int(input())
# c=input()

# if c=='+':
#   print(a,c,b,'=',a+b)
# elif c=='-':
#   print(a,c,b,'=',a-b)
# elif c=='*':
#   print(a,c,b,'=',a*b)
# elif c=='/':
#   if b==0:
#     print('на ноль дельить нельзя')
#   else:
#     print(a,c,b,'=',a/b)

# def calc(a,b,c):
#   if c=='+':
#     return a+b
# print(a,c,b,'=',calc(a,b,c))

# 1.годы, номер которых кратен 4, — високосные
# 2.номер которых кратен 100, — невисокосные
# 3.номер которого кратен 400, — високосный
# невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300)

# Годы 1600 и 2000 — високосные

# year = int(input())
# #Високосный Невисокосный
# if year%4!=0 and year%100==0 or year%400!=0:
#   print('невисокосный')
# else:
#   print('високосный')
# #print(2022//4)

# def leap_year (year):
#   if year%4 == 0 and year % 100 != 0 or year % 400 == 0:
#     return print(year, 'високосный')
#   else:
#     return print(year, 'невисокосный')

# #leap_year(int(input()))
# for i in range(2000,2030):
#   leap_year(i)

# вклад n рублей на m лет под 25%
# каждый год кго вклад увеличивается на 25%
# эти деньги прибавляются к вкладу

# 1000 на 2 года
#   1год: 1000*1,25=1250
#     2год: 1250*1.25 = 1562.5
#   за 2 года 1000*1.25*1.25=1562.5
