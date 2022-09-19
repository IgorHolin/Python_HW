# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Enter your number please: '))

def listing(num):
    arr = []
    i = 2
    while num != 1:
        if num % i == 0:
            arr.append(i)
            num = num / i
        else:
            i += 1
    return arr

print(listing(number))




