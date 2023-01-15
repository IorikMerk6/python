# def hellow_orld():
#     print("Hello world")
#
#
# hellow_orld()
# def plus(number1, nigger2):
#     result = number1 + nigger2
#     return result
#     print(result)
#
# plus(5,3)
# plus(nigger2 = 4, number1= 1)
# def ya_gan(name):
#     if name == "Антон" or name == "Anton":
#         return True
#     print(name)
# if ya_gan("Богдан"):
#     print("Это база")

# def check(list):
#     sort = sorted(list)
#     if list == sort:
#         return True
#
# list = [1,2,6,1.2,3,4]
# if check(list) == True:
#     print("Кайфоват хацу")
# else:
#     print("Тебе не быть программистом")
# def find_longest(list):
#     spisok2 = []
#     for i in list:
#         spisok2.append(len(i))
#     maxy = max(spisok2)
#     inf = spisok2.index(maxy)
#     return list[inf], spisok2[inf]
# list = ["Партия", "миска", "рис", "негр","кошка","жена"]
# print(find_longest(list))
# def is_prime(wert):
#     for i in range(2,wert+1):
#         if wert == i:
#             return True
#         if wert % i == 0:
#             break
#
#
#
# if is_prime(2538):
#     print("Это база")
# else:
#     print("Дефолт")
# def bashni(sp:list,razdel:str)->str:
#     resnya = ""
#     for i in sp:
#         resnya += i + razdel
#     print(resnya)
#
# reigan = ["бебра","Аргентина","абоба"]
# bashni(reigan, "😎")
def factor(num):
    o = 1
    for i in (2,num+1):
        o *= i
    return o
num = int(input("Напиши число:"))
print(factor(num))

