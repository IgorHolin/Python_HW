# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# aaaaassssfffffeeewqqqer -> 5a4s5f3ew3qer
# 5a4s5f3ew3qer -> aaaaassssfffffeeewqqqer


with open('/Users/User/Desktop/GeekBrains/Знакомство с языком Python/Семинары/HW/HW_5/task_4_input.txt', 'w', encoding='UTF-8') as f:
    f.write('aaaaassssfffffeeewqqqer')

with open('/Users/User/Desktop/GeekBrains/Знакомство с языком Python/Семинары/HW/HW_5/task_4_input.txt', 'r', encoding='UTF-8') as f:
    inp = list(map(str, f.readline()))


# # Алгоритм сжатия

def rle_zip(some_string):
    count = 1
    result = []

    for x, item in enumerate(some_string):
        if x == 0:
            continue
        elif item == some_string[x - 1]:
            count += 1
        else:
            result.append((some_string[x - 1], count))
            count = 1

    result.append((some_string[len(some_string) - 1], count))
    return result


def rle_print(some_list):
    final = []
    for item in some_list:
        if item[1] == 1:
            final.append(item[0])
        else:
            final.append(str(item[1]) + item[0])
    return ''.join(final)

# Алгоритм развёртывания

def rle_unzip(some):
    res = []
    for i in some:
        res.append(i[0] * i[1])
    return ''.join(res)



with open('/Users/User/Desktop/GeekBrains/Знакомство с языком Python/Семинары/HW/HW_5/task_4_output.txt', 'w', encoding='UTF-8') as f:
    f.write(rle_print(rle_zip(inp)))

with open('/Users/User/Desktop/GeekBrains/Знакомство с языком Python/Семинары/HW/HW_5/task_4_output_2.txt', 'w', encoding='UTF-8') as f_2:
    f_2.write(rle_unzip(rle_zip(inp)))