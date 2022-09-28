# List Comprehension
# n = int(input('Enter the number of digits: '))

# lst = [int(input('enter the digit: ')) for _ in range(n)]
# print(lst)

# new_lst = [lst[i] if lst[i] % 2 == 0 else lst[i]**2 for i in range(len(lst)) ]
# print(new_lst)

# new_lst2 = [lst[i] for i in range(len(lst)) if lst[i] % 2 == 0]
# print(new_lst2)




# Map
lst = [2,1,3,4,5]
new_lst = list(map(lambda x: x*x, lst))
print(new_lst)



# Filter
# lst = [2,14,15,16,16,17,2,5,1,3,4,5]
# new = list(filter(lambda x: x%2==0, lst))
# print(new)



# Filter + Map
# lst = [2,14,15,16,16,17,2,5,1,3,4,5]
# new = list(map(lambda x: x*x, filter(lambda x: x%2==0, lst)))
# print(new)




# Enumerate
# lst = 'Hello World!'
# for i, item in enumerate(lst):
#     print(i, item)



# Task_1    

#        0 1 2 3 4
# srt = '1 3 4 5 6'
# arr = list(map(int, srt.split()))

# for i in range(len(arr)-1):
#     if arr[i+1] - arr[i] > 1:
#         num = arr[i] + 1
# print(num)





# Task_3
# x = 'krg'

# lst = 'ajsdnkrg kasmdkrg kakwnkner je erneunte ejntkmhlmnf'
# res = ' '.join((list(filter(lambda x: 'krg' not in x, lst.split()))))
# print(res)


# Task_2



