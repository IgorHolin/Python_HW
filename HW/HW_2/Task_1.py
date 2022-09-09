# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:
# 6782 -> 23
# 0,56 -> 11

# Исходя из условия мы не знаем как велико будет число, тем более это может быть float. Решил через строки

while True:

    a = input('Enter the number please: ')
    new_str = str
    res = 0
    for i in range(len(a)):
        if (a[i] == '.') or (a[i] == ","):
            new_str = a.replace(a[i], '')
    for n in range(len(new_str)):
        res += int(new_str[n])
    print(res)