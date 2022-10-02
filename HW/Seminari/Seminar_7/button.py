from ui import *
from calc import *


def start_calc():
    num_type = which_type()
    if num_type == "1":
        print('Вы работаете с рациональными числами')
    else:
        print('Вы работаете с натуральными числами')
    value_a = get_value(num_type)
    value_b = get_value(num_type)
    init(value_a, value_b)
    action = get_action()
    if action == "+":
        print('Вы выбрали сложение')
        output_result(sum_f())
    elif action == "-":
        print('Вы выбрали вычитание')
        output_result(dif_f())
    elif action == "*":
        print('Вы выбрали вычитание')
        output_result(mult_f())
    else:
        print('Вы выбрали деление')    
        output_result(div_f())