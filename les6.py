#month = input("Введи номер месяца:")
#if month.isdigit() and 1<= int(month) <= 12:
 #   month = int(month)
  #  if 3<=month<=5:
   #     print("Весна")
    #elif 6 <= month <= 8:
     #   print("Лето")
    #elif 9<=month<=11:
     #   print("Осень")
    #elif month == 13:
     #   print("32 марта")
    #else:
     #   print("Зима")
#else:
 #   print("Э, удали компьютер")
# #h = int(input("Часы:"))
# #m = int(input("Минуты:"))
# #s = int(input("Секунды:"))
# #if 0<= h <=23 and 0<= m <= 59 and 0<= s <= 59:
#     print("Всё верно")
#     print(h,":",m,":",s)
# else:
#     print("Неправильно. Попробуйте ещё раз или удалите компьютер")
score = 0
q1 = input("Сколько я съел вчера пельменей?\n"
           "1)Запятая\n"
           "2)12\n"
           "3)10\n"
           "Говори:")
if q1 == "2":
    score += 1
    print("Плюс очко")
else:
    score -= 1
    print("Вы потеряли очко")
q2 = input("Было 2 козла. Сколько?\n"
           "1)Канарейка\n"
           "2)2 барана\n"
           "3)0\n"
           "Сколько?:")
if q2 == "3":
    score += 1
    print("Плюс очко")
else:
    score -= 1
    print("Вы потеряли очко")
q3 = input("Сколько негров?\n"
           "1)99\n"
           "2)1\n"
           "3)Были только белые\n"
           "Ответ:")
if q3 == "1":
    score += 1
    print("Плюс очко")
else:
    score -= 1
    print("Вы потеряли очко")
print("Ваше очко =", score)