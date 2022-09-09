# Задание 3 
# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.

# Пример:
# Для n = 6 -> 14.072

list = []
res = 0
n = int(input("Enter the number of digits: "))

for i in range(1, n+1):
    list.append((1 + 1/i)**i)
    
for k in range(len(list)):
    res += list[k]

print(round(res, 3))