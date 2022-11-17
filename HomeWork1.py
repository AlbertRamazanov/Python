# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

""" a=int(input ("Введите порядковый номер дня недели "))
if a>5:
  print(f"{a} Явдяется выходным днём")
else: 
   print (f"{a} Явдяется рабочим днём")"""

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

"""x=int(input ("Введите координат точки x "))
y=int(input ("Введите координат точки y "))
if (x>0 and y>0):
   print ("Координаты точек находятся в первой четверти")
elif (x<0 and y>0):
   print ("Координаты точек находятся во второй четверти")
elif (x<0 and y<0):
   print ("Координаты точек находятся в третьей четверти") 
else: 
   print ("Координаты точек находятся в четвёртой четверти")"""


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

"""a=int(input ("Введите номер четверти ")) 
if a==1:
   print ("Диапазон возможных координат в первой четверти: x>0, y>0 ")
elif a==2:
   print ("Диапазон возможных координат в первой четверти: x<0, y>0 ")
elif a==3:
   print ("Диапазон возможных координат в первой четверти: x<0, y<0 ") 
elif a==4: 
   print ("Диапазон возможных координат в первой четверти: x>0, y<0 ")"""

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

"""import math

x_coordinate_A = float(input('Введите координату точки А по оси Х: '))
y_coordinate_A = float(input('Введите координату точки А по оси Y: '))
x_coordinate_B = float(input('Введите координату точки B по оси Х: '))
y_coordinate_B = float(input('Введите координату точки B по оси Y: '))

distance = round(math.sqrt((x_coordinate_B - x_coordinate_A)**2 + (y_coordinate_B - y_coordinate_A)**2), 2)
print(distance)"""

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

import os 

os.system('clear')

def Truth ():
    result = 0
    result = True

    for n in range(0, 8):
        num = bin(n)
        num = num.replace('b', '0')
        X = int(num[-3])
        Y = int(num[-2])
        Z = int(num[-1])
        left_part = not(X or Y or Z)
        right_part = (not X) and (not Y) and (not Z)
        if left_part == right_part:
            result += 1
        print(X, Y, Z, left_part, right_part, left_part == right_part, result)
    print()
    if result == 8:
        return print(True)
    else:
        return print(False)
        result = result and (not(X or Y or Z)) == ((not X) and (not Y) and (not Z))

    print(result)


Truth()



  