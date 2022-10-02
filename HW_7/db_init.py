from random import randint


def randomize():
    names = ['Иван', 'Геннадий', "Алексей", "Оксана", "Анна", "Мария"]
    surnames = ["Попов(а)", "Иванов(а)", "Сидоров(а)", 'Белкин(а)', 'Стрелкин(а)']
    jobs = ["Адвокат","Юрист", "Кассир", "Водитель"]
    phone_num = ['+48566987756', '+48125664789', '+481478881234', '+48779663267', '+48555127884']
    return f'{surnames[randint(0, len(surnames) -1)]};{names[randint(0, len(names) -1)]};{phone_num[randint(0, len(phone_num) -1)]};{jobs[randint(0, len(jobs) -1)]}\n\n'


with open('C:\Users\User\Desktop\GeekBrains\Знакомство с языком Python\Семинары\HW_7\database.txt','w', encoding="UTF-8") as db:
    for _ in range(251):
        db.write(randomize())
