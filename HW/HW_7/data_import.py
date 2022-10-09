

def import_html():
    with open('C:\\Users\\User\\Desktop\\GeekBrains\\Знакомство с языком Python\\Семинары\\HW\\HW_7\\data_.html', 'r', encoding="UTF-8") as page:
        a = page.readlines()
    return ''.join(a)


def import_xml():
    with open('C:\\Users\\User\\Desktop\\GeekBrains\\Знакомство с языком Python\\Семинары\\HW\\HW_7\\data_.xml', 'r', encoding="UTF-8") as page:
        b = page.readlines()
    return ''.join(b)


