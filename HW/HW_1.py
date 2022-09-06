# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели
# и проверяет, является ли этот день выходным.

# *Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

while True: #сделал бесконечный цикл чтоб не перезапускать программу миллион раз
    day = int(input("Enter the number of the day please: "))
    if 1 <= day <= 5:
        print('You have to go to work :(')
    elif 6 <= day <=7:
        print("It's day off!! :)")
    else:
        print("There are only 7 days in week -_-'")
 
