# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Текстовый файл 'task_1.txt'




with open('/Users/User/Desktop/GeekBrains/Знакомство с языком Python/Семинары/HW/HW_5/task_1.txt', 'w', encoding='UTF-8') as f:
    f.write('Добавьте игруабв противабв бота. Достаточно сделать так, чтобы бот не брал конфет большеабв положенногоабв илиабв большеабв чемабв имеетсяабв вабв кучеабв.')


with open('/Users/User/Desktop/GeekBrains/Знакомство с языком Python/Семинары/HW/HW_5/task_1.txt', 'r', encoding='UTF-8') as f:
    a = ' '.join(list(filter(lambda x: 'абв' not in x, f.readline().split())))
    
with open('/Users/User/Desktop/GeekBrains/Знакомство с языком Python/Семинары/HW/HW_5/task_1_output.txt', 'w', encoding='UTF-8') as f:
    f.write(a)