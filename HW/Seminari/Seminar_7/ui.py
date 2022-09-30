from calc import x,y

def which_num():
    which_num = input('Чтобы выбрать рациональные числа введите "1", чтобы выбрать натуральные введите "2": ')
    while which_num not in "12":
        which_num = input('Введите "1" - рациональные числа или "2" - натуральные числа: ')
    if which_num == "1":
        type(x), type(y) == int
        print('Вы работаете с натуральными числами')
    elif which_num == "2":
        type(x), type(y) == float
        print('Вы работаете с рациональными числами')
    return which_num
        

def get_action():
    which_action = input('Какое действие вы хотите совершить? Введите знак: ')
    while which_action not in "+-*/":
        which_action = input('Введите один из 4-ёх знаков: "+"  "-"  "*"  "/": ')
    if which_action == "+":
        print('Вы выбрали сложение')
    elif which_action == "-":
        print('Вы выбрали вычитание')
    elif which_action == "*":
        print('Вы выбрали вычитание')
    else:
        print('Вы выбрали деление')
    return which_action

def get_value():
    return int(input('Введите число: '))