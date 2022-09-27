# Крестики нолики



desk = list(range(1,10))

#задаём доску

def draw_desk(some_desk):
   print("-" * 13)
   for i in range(3):
      print("|", some_desk[0+i*3], "|", some_desk[1+i*3], "|", some_desk[2+i*3], "|")
      print("-" * 13)

# задаём ввод пользователя, с проверкой ввёл ли он число и не занята ли клетка

def take_input(token):
   flag = False
   while not flag:
      player_answer = input("Куда ставить знак " + token + "? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(desk[player_answer-1]) not in "XO"):
            desk[player_answer-1] = token
            flag = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

# задаём выигрышные значения

def check_win(desk):
   win_condition = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for condition in win_condition:
       if desk[condition[0]] == desk[condition[1]] == desk[condition[2]]:
          return desk[condition[0]]
   return False

# собираем игру

def game(desk):
    counter = 0
    win = False
    while not win:
        draw_desk(desk)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(desk)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_desk(desk)
game(desk)

input("Нажмите Enter для выхода")