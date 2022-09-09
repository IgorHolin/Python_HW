# Задание 6 Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

# Пример
# -Для "abababb" и "aba" -> 2

a = input("Enter the string please: ")
b = input("Enter the sub-string please: ")

ind = 1
count = 0

while ind != -1:
    ind = a.find(b)
    if ind >= 0:
        count += 1
    a = a[ind+1:]
print(count)
 