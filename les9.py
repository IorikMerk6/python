# import random
# import time
# is_game = "y"
# print("Время пострелять. Заряжаем револьвер...")
# while is_game == "y":
#     time.sleep(0.5)
#     print("Раскручиваем барабан")
#     time.sleep(2.5)
#     print(1)
#     time.sleep(1)
#     print(2)
#     time.sleep(1)
#     print(3)
#     print("Выстрел!")
#     camori = [1, 2 , 3, 4 , 5 ,6 ]
#     patron = random.choice(camori)
#     our = random.choice(camori)
#     if patron == our:
#         print("Потрачено")
#         is_game = "n"
#     else:
#         print("Повезло")
#         x = input("Играть дальше?y - да, n - нет")
#         if x == "n":
#             is_game = "n"
# print("Как ощущения?")
# lst = ["Антон1", "Антон2", "Антон3", "Антон4"]
# for antoha in lst:
#     print(antoha)
# for i in range(0, 10):
#     print(i)
# x = 0
# while x != 10:
#     print("Негры", x)
#     x += 1
#word = input("Введите слово")
#while word:
   # print(word)
   #word = word[:-1]
# x = int(input("Введи циферку:"))
# while x:
#     x -= 1
#     if x%2 == 0:
#         print(x, end=" ")
# x = int(input("Введите цифру: "))
# step = 0
# while x != 1:
#     step += 1
#     if x%2 == 0:
#
#         x = x//2
#         print(x)
#     else:
#         x = 3 * x + 1
#         print(x)
# print("Шагов", step)
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
lst = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
hand_player = [random.choice(lst)]
hand_computer = [random.choice(lst)]
score_player = 0
score_computer = 0
get_card = "y"
is_game = "y"
if is_game == "y":
    while get_card == "y":
        hand_player.append(random.choice(lst))
        if sum(hand_player) > 21 and 11 in hand_player:
            for i in range(0, len(hand_player)):
                if hand_player[i] == 11:
                    hand_player [i] = 1
        score_player = sum(hand_player)
        print(f"Твоя рука: {hand_player}. Очков : {score_player}")
        print("Первая карта компудахтера:", hand_computer[0])
        if score_player > 21:
            get_card = "n"
        else:
            get_card = input("y - взять карту, n - не брать ")
        while sum(hand_computer) < 17:
            hand_computer.append(random.choice(lst))
            if sum(hand_computer) > 21 and 11 in hand_computer:
                for i in range(0, len(hand_computer)):
                    if hand_computer[i] == 11:
                        hand_computer[i] = 1
            score_computer = sum(hand_computer)
            print("=" * 20)
            print(f"Твоя итоговая рука: {hand_player}.Очков : {score_player}.")
            print(f"Компудахтерная итоговая рука: {hand_computer}.Очков : {score_computer}.")
            if score_computer>21 and score_player >21:
                print("Ничья.Перелёт обоих")
            elif score_player > 21:
                print("Твой перебор. Проиграл")
            elif score_computer > 21:
                print("Перебор компа. Выиграл")
            elif score_player > score_computer:
                print("Победа")
            elif score_player < score_computer:
                print("Проиграл")
            else:
                print("Ничья")
        is_game = input("Ещё разочек за наше очко? y - da, n- net:")
else:
    quit()
























