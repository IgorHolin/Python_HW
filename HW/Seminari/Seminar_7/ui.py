from calc import x,y

def which_type():
    w_type = input('Чтобы выбрать рациональные числа введите "1", чтобы выбрать натуральные введите "2": ')
    while w_type not in "12":
        w_type = input('Введите "1" - рациональные числа или "2" - натуральные числа: ')
    if w_type == "1":
        type(x), type(y) == int
    elif w_type == "2":
        type(x), type(y) == float
    return w_type
        

def get_action():
    which_action = input('Какое действие вы хотите совершить? Введите знак: ')
    while which_action not in "+-*/":
        which_action = input('Введите один из 4-ёх знаков: "+"  "-"  "*"  "/": ')
    return which_action

def get_value(value_type):
    if value_type == "1":
        return float(input('Введите число число с плавающей точкой: '))
    else:
        return int(input('Введите целое число: '))


def output_result(result):
    print(result)

