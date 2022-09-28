# Было

list = []
res = 0
n = int(input("Enter the number of digits: "))

for i in range(1, n+1):
    list.append((1 + 1/i)**i)
    
for k in range(len(list)):
    res += list[k]

print(round(res, 3))


# Стало

arr = [((1 + 1/i)**i) for i in range(1, int(input('Enter the number of digits: ')) + 1)]
print(arr)
print(round(sum(arr), 3))

