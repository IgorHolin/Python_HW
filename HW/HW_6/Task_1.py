# Было

from math import factorial

n = int(input('Enter the number please: '))
list = []

for i in range(1, n+1):
    list.append(factorial(i))
print(list)


# Стало

from math import factorial

n = int(input('Enter the number please: '))
print([factorial(i) for i in range(1,n+1)])