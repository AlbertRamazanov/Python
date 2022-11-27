# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

"""n = int(input('Введите число: ')) 
a = list(range (n))
sum=0
for i in a:
    if i % 2!=0:
        sum=sum+i
    i+1    
print (f"{a} Сумма нечётных чисел равна ", sum)"""

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

"""from random import randint


number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list)
print(list2)"""

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

"""import random
number = int(input('Введите размер списка '))
x=[round(random.uniform(1.99, 10), 2) for x in range(number)]
max_number = max(x)
min_number = min(x)   
a = max_number - min_number
round (a, 2)
print(f'{x} "Разница между максимальным и минимальным вещественным числом равна {a} "')"""

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

"""s = ""
n = int(input('Введите число: '))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)"""

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

n = int(input('Введите число: '))

def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n-1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums

fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))
print(fibo_nums.index(0))
