# 5 Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt

while True: #чтоб не перезапускать программу

    a1 = float(input("Enter 'X' coordinate of first point: "))
    b1 = float(input("Enter 'Y' coordinate of first point: "))
    a2 = float(input("Enter 'X' coordinate of second point: "))
    b2 = float(input("Enter 'Y' coordinate of second point: "))

    distance = round(sqrt((a2-a1)**2 + (b2-b1)**2), 3)
    print(distance)
