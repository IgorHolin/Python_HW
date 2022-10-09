
def show_data():
    with open('C:\\Users\\User\\Desktop\\GeekBrains\\Знакомство с языком Python\\Семинары\\HW\\HW_7\\database.txt', 'r', encoding="UTF-8") as db:
        data = ''.join(db.readlines())
    return data

# print(show_data())