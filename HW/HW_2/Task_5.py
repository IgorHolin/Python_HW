# Задание 5 
# Реализуйте алгоритм перемешивания списка.

from random import randint, shuffle


n = int(input("Enter the number of digits in list: "))
list = []

for i in range(n):
    list.append(randint(1,100))
print(f'List looks like following: {list}')

res_list = list[:]
shuffle(res_list)
print(f'Shuffled list looks like following: {res_list}')



