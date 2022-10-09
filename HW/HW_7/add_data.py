

def add_data():
    with open('C:\\Users\\User\\Desktop\\GeekBrains\\Знакомство с языком Python\\Семинары\\HW\\HW_7\\database.txt', 'a', encoding="UTF-8") as db:
        new_line = input('Введите данные по примеру "Фамилия;Имя;Номер телефона;Должность". Используйте ";" для разделения. Не используйте пробеллов')
        db.write(new_line)
