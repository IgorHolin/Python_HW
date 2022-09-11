# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

#Решил сделать конкатинацией списков :)

a = int(input("Enter the number of digits: "))


def fibo_list(num):

    plus_list = [0, 1]
    for i in range(2, num+1):
        plus_list.append(plus_list[i-1] + plus_list[i - 2])

    minus_list = [1, -1]
    for i in range(2, num):
        minus_list.append(minus_list[i-2] - minus_list[i - 1])
    minus_list.reverse()
    return minus_list + plus_list

print(fibo_list(a))
