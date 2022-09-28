# Было

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def odd_sum(arr):
#     res = 0
#     for i in range(1,len(arr),2):
#         res += arr[i]
#     return res

# print(odd_sum(list))


# Стало

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(filter(lambda x: list_.index(x) % 2 != 0, list_)))