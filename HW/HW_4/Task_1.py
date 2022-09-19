# 1 Вычислить число π c заданной точностью d

# *Пример:* 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

#Честно говоря даю решение как понял задачу, не судите строго.

from math import sqrt
from random import random

d = int(input('Enter the number of numbers after "." :'))

def calculation(num):
    total = 1000000
    inside = 0
    for i in range(1, total):
        x,y = random(), random()
        distance = sqrt(x**2 + y**2)
        if distance <= 1:
            inside += 1
    pi = 4 * (inside/total)
    my_pi = round(pi, num)
    return my_pi

print(calculation(d))
