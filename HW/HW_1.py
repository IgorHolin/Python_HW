# 4 Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y).


while True: #бесконечный цикл, чтоб не перезапускать программу

    qrt = float(input('Enter the quarter please: '))
    if 1 <= qrt <= 4:
        if qrt == 1:
            print('x = [0; +infinity] and y = [0; +infinity]')
        elif qrt ==2:
            print('x = [0; -infinity] and y = [0; +infinity]')
        elif qrt == 3:
            print('x = [0; -infinity] and y = [0; -infinity]')
        else:
            print('x = [0; +infinity] and y = [0; -infinity]')
    else:
        print('There are only 4 quartees ^_^')