from ui import *
from calc import *


def start_calc():
    num_type = which_type()
    if num_type == "1":
        print('Вы работаете с натуральными числами')
    else:
        print('Вы работаете с рациональными числами')
    value_a = get_value(num_type)
    value_b = get_value(num_type)
    init(value_a, value_b)
    action = get_action()
    if action == "+":
        print('Вы выбрали сложение')
        return(sum_f(value_a, value_b))
    elif action == "-":
        print('Вы выбрали вычитание')
        return(dif_f(value_a, value_b))
    elif action == "*":
        print('Вы выбрали вычитание')
        return(mult_f(value_a, value_b))
    else:
        print('Вы выбрали деление')
        return(div_f(value_a, value_b))