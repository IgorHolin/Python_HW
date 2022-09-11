# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from math import ceil

list = [2, 3, 4, 5, 6]

def pair_mult(arr):
    res_list = []
    last_ind = len(arr) -1
    for i in range(ceil((len(arr)/2))):
        res_list.append(arr[i] * arr[last_ind])
        last_ind -= 1
    return res_list

print(pair_mult(list))

