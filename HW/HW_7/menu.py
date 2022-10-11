from ui import define_option as do
from add_data import add_data
from show_data import show_data
from data_export import create_html as cs, create_xml as cx
from data_import import import_html as ih, import_xml as ix


def choice():
    choice = input('Желаете выполнить другую операцию?\nВведите "YES" для выбора или нажмите Enter чтобы выйти из программы: ')
    choice = choice.lower()
    while choice != 'yes' and choice != '':
        choice = input('Введите "YES" для выбора другой операции или Enter для выхода: ')
        choice = choice.lower()
    if choice == 'yes':
        tmp = input('Вам доступны действия:\n1. Просмотр записей\n2. Добавление записей\n3. Экспорт записей\n4. Импорт записей\n')
        while tmp != '1' and tmp != '2' and tmp != '3' and tmp != '4':
            tmp = input('Введите номер опреации, пожалуйста: ')
        return tmp
    else:
        print('Спасибо за использование нашей базы. Всего хорошего!')
        return
