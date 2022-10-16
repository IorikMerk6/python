#x = 7
#if x<10:
 #   print("Пон")
#else:
 #   print("Антон")
#phrase = "Я карта"
#if phrase == "z rfhnf":
#    print("Ладно")
#else:
   # print("Dota 2")
#number = int(input())
#if number>0:
 #   print("П")
#elif number == 0:
 #   print("0")
#else:
  #  print("Отрц.")
#year = int(input("Ввести год"))
#if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
  #  print("Високосный")
#else:
  #  print("Не високосный")
#num_1  = int(input("Vvedite pervoe chislo"))
#operation = input("Operatcia:").strip()
#num_2 = int(input("Vvedite vtoroe chislo:"))
#lst = ["-", "+", "*", "/"]
#if operation in lst:
   # if operation == "-":
     #   print(num_1 - num_2)
   # elif operation == "+" :
        #print(num_1 + num_2)
    #elif operation == "*" :
      #  print(num_1 * num_2)
    #else:
      #  print(num_1 / num_2)
#else:
    #print("Переделывай")
#
#
ticket = input("Введи номер билета(6 знаков):")
if len(ticket) == 6 and ticket.isdigit():
    first_half = ticket[:3]
    last_half = ticket[:-3]
    first_sum = first_half[0] + first_half[1] + first_half[2]
    last_sum = last_half[0] + last_half[1] + last_half[2]
    if first_sum == last_sum:
        print("Счастливый билет")
    else:
        print("Билет не счастливый")
else:
    print("Иди куда подальше")