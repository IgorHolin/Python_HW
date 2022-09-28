
line = '1-2*3'

def pol_to_list(line):
    res = []
    for item in line:
        if item.isdigit():
            res.append(int(item))
        else:
            res.append(item)
    return(res)

print(pol_to_list(line))

def calc(lst):
    tmp = []
    index = 0
    while index < len(lst):
        if type(lst[index]) is int:
            tmp.append(lst[index])
        elif lst[index] == '+':
            tmp.append(lst[index + 1])
            index += 1
        elif lst[index] == '-':
            tmp.append(-lst[index + 1])
            index += 1
        elif lst[index] == '*':
            tmp[-1] = tmp[-1] * lst[index + 1]
            index += 1
        elif lst[index] == '/':
            tmp[-1] = tmp[-1] / lst[index + 1]
            index += 1
        index += 1
    return sum(tmp)

print(calc(pol_to_list(line)))