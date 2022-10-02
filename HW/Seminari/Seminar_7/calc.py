x = 0
y = 0
title = ''

def init(a,b):
    global x
    global y
    x = a
    y = b


def sum_f():
    title = 'Сумма = '
    return f'{title}{x + y}'


def dif_f():
    title = 'Разность = '
    return f'{title}{x - y}'


def mult_f():
    title = 'Произведение = '
    return f'{title}{x * y}'


def div_f():
    title = 'Частное = '
    return f'{title}{x / y}'
