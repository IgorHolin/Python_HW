from ui import define_option as do
from add_data import add_data
from show_data import show_data
from data_export import create_html as cs, create_xml as cx
from data_import import import_html as ih, import_xml as ix


def process():
    if do() == 1:
        print(f'База данных:\n{show_data()}')
    elif do() == 2:
        print("Вы выбрали добавление данных!")
        add_data()
    elif do() == 3:
        wh_one = input('Какой формат экспортировать? Введите цифру:\n1. XML\n2.HTML')
        while wh_one != '1' and wh_one != '2':
            wh_one = input('Введите "1" для экспорта XML, или "2" для экспорта HTML')
        if wh_one == '1':
            cx()
        else:
            cs()
    else:
        w_one = input('Какой формат импортировать? Введите цифру:\n1. XML\n2.HTML')
        while w_one != '1' and w_one != '2':
            w_one = input('Введите "1" для импорта XML, или "2" для импорта HTML')
        if w_one == '1':
            print(ix())
        else:
            print(ih())