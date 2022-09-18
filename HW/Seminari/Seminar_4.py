
# w - открытие на запись, создание
# r - открытие на чтение
# a - открытие на дозапись
# b - бинарный для работы с байтовыми
# t - текстовый для работы с текстами 


# f = open('my_file.txt', 'r')
# f_out = open('file_2.txt', 'a')

# # f.write('hello\n')
# f_out.writelines(f.readlines())



# f.close()  # обязательное закрытие файла
# f_out.close()


# with open('my_file.txt', 'a') as f:  # питон автоматически закрывает файл если использовать with
#     f.write('kmefemf\n')
#     f.write('kmsdfsdf\n')
#     f.write('kmasdwdq\n')


# with open('my_file.txt', 'r') as f:  # питон автоматически закрывает файл если использовать with
#     print(f.readline())

a,b = int(input()),int(input())
tmp = a*b
if (a%b == 0):
    print(tmp/a)
elif (b%a == 0):
    print(tmp/b)
elif a != b:
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
print(tmp / a)