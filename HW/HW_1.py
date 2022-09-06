# 3 Напишите программу, которая принимает на вход координаты точки (X и Y)
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости
# в которой находится эта точка (или на какой оси она находится).

# *Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


while True: #использую бесконечный цикл, чтоб не перезапускать программу

    x = float(input("Enter 'x' please: ")) 
    y = float(input("Enter 'y' please: "))
    #использую float значение так как не сказано что числа целые
    
    if x > 0 and y > 0:
        print('1st quarter')
    elif x < 0 and y > 0:
        print('2nd quarter')
    elif x < 0 and y < 0:
        print('3rd quarter')
    else:
        print('4th quarter')
