# Задание 4 
# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

n = int(input('Enter the number of digits in list: '))

list = []
for i in range((n*2)+1):
    list.append(-n)
    n-=1

print(list)

a = int(input('Enter the position of 1st element: '))
b = int(input('Enter the position of 2nd element: '))

print(f'The result of multiplication of {a} position and {b} position is: {list[a-1]*list[b-1]}')

# в строке 18 стоит "index-1" тк пользователь обычно считает не от 0 а от 1