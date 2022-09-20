# 4 Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

power = int(input('Enter the power: '))

def randomize(power):
    first = randint(0,100)
    second = randint(0,100)
    third = randint(0,100)
    final_expression = f'{first}*x^{power} + {second}*x^{randint(0,power-1)} + {third} = 0'
    return final_expression


with open('task_4.txt', 'a') as file:
    file.writelines(f'{randomize(power)}\n')

