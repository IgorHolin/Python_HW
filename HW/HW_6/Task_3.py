# Было

# arr_in = input('Enter the numbers using spaces: ')

# def no_repeats(some_arr):
#     arr = some_arr.split()
#     new_arr = []
#     for i in range(len(arr)):
#         a = arr.count(arr[i])
#         if a == 1:
#             new_arr.append(arr[i])
#     return new_arr

# print(no_repeats(arr_in))


# Стало

arr = list(map(int, input('Enter the numbers using spaces: ').split()))
new_arr = [arr[i] for i in range(len(arr)) if arr.count(arr[i]) == 1]
print(new_arr)
