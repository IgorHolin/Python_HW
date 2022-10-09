from show_data import show_data as sd

def create_html():
    style = 'style="font-size:18px;"'
    html = '<html>\n  <head></head>\n  <body>\n'
    html += '    <p {}>База:\n {} </p>\n'\
        .format(style, sd())

    with open('C:\\Users\\User\\Desktop\\GeekBrains\\Знакомство с языком Python\\Семинары\\HW\\HW_7\\data_.html', 'w', encoding="UTF-8") as page:
        page.writelines(html)
# create_html()

def create_xml():
    xml = '<xml>\n'
    xml += '    База:\n{}'\
        .format(sd())

    with open('C:\\Users\\User\\Desktop\\GeekBrains\\Знакомство с языком Python\\Семинары\\HW\\HW_7\\data_.xml', 'w', encoding="UTF-8") as page:
        page.write(xml)
# create_xml()
