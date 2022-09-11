# 3. Задайте список из вещественных чисел. Напишите программу
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

#Строго говоря миниальный остаток в примере это 0 у пятёрки, по этому ответ дан неверный. Верный ответ в данном случае 0.2

 
# Решение сделано под пример

list = [1.1, 1.2, 3.1, 5, 10.01]
def find_diff(arr):
    
    for i in range(len(arr)):
        arr[i] = arr[i] - int(arr[i])
        arr[i] = round(arr[i], 2)
    maxima = max(arr)

    for k in range(len(arr)):
        minima = arr[0]
        if arr[k] < minima and arr[k] != 0:
            minima = arr[k]
    
    return maxima - minima

print(find_diff(list))