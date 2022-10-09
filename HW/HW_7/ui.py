

def define_option():
    print('Вам доступны действия:\n1. Просмотр записей\n2. Добавление записей\n3. Экспорт записей\n4. Импорт записей\nДля выхода нажмите Enter')
    select = input('Выберите номер операции: ')
    while select != '1' and select != '2' and select != '3' and select != '4' and select != '':
        select = input('Введите номер опреации, пожалуйста: ') 
    return int(select)
