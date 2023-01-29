# def hello(x):
#     return "hello" + x
#
# print(hello("Джо Байден"))
#
# l = lambda x, b: "hello" + b + x
# print(l("Антон", "Еврей"))
# # генератор списков (list comprehension)
# r = [i for i in range(1, 6)]
# print(r)
# import time
# import random
# print ("Время проверить твою ловкость и скорость и понять, кто самый быстрый стрелок на западе! Когда увидишь 'СТРЕЛЯЙ', у тебя будет 0.48 секунды чтобы нажать Enter. Но если ты нажмёшь Enter раньше, то ты проиграл.")
# input("Нажми enter, чтобы начать")
# print("Время пострелять...")
# time.sleep(random.randint(1,5))
# start = time.time()
# input("Стреляй!")
# end = time.time()
# trime = end - start
# print(f"{trime} секунд ")
# if trime > 0.51:
#     print("Ты мох опущенный")
# elif trime == 0.00:
#     print("Фальш старт, ты уху ел")
# else:
#     print("Крутой")
import random
print("Напиши, сколько костей хочешь бросить:")
f = int(input())
slov = {}
for i in range(f,f * 6):
    print(i)
    slov[i] = 0
print(slov)







