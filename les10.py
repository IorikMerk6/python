# lst = [-1,0,1,2,3,4,5,6,7]
# for i in lst:
#     print(i)
# for m in range(0, 10):
#     print(m)
# x = int(input("Введи число:"))
# y = int(input("Введи число:"))
# while x<=y:
#     print(x, end= "🧕🏿")
#     x += 1
# for c in range(x,y):
#     print(c)
# number = int(input("Ярусов:"))
# while True:
#     symbol = input("Символ:").strip()
#     if len(symbol)==1:
#         break
#     else:
#         print("Еррор")
# for m in range(1, number +1):
#     print(" " * (number-m))
#     print(symbol*m, end ="")
#     print(symbol * m)
#x = int(input("Введи число:"))
#y = 1
#for i in range(1, 10+1):
  #  print(x,"*",y,"=",x*y)
  #  y+=1
#width = int(input("Ширина:"))
#height = int(input("Высота:"))
#for _ in range(height):
   # print("#" * width)
import random
intro =  """
   ▓▀▀▀▀▄   ▐█    ██   ▄▓▀▀▀▀▄   █▒▀▀▀▒      ▓▀▓      ▐█    ██                  ▓▀▓
   ▒▌▄▄▄▀   ▐█  ▄█▀█  ▓▌         █▌         ▓▌ ▐▓     ▐█  ▄█▀█                 ▓▌ ▐▓ 
   ▒▌  ▀█▄  ▐█╔▓▀ ▐█  █          █▌█▌█▌    ▓▌   ▐▓    ▐█╔▓▀ ▐█                ▓▌▄▄▄▐▓ 
   ▒▌  ▄█▀  ▐██   ▐█  ▀▓▄    ▄   █▌       ▓▌     ▐▓   ▐██   ▐█               ▓▌     ▐▓
   ▀▀▀▀     ▀▀     ▀     ▀▀▀▀    ▓▒▄▄▄▒  ▐█       █▌  ▀▀     ▀  ▄▄▄▄▄▄▄▄▄▄  ▐█       █▌
"""
print(intro)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
vocabulary = ['Anton', 'Alex', 'Alexandr', 'Arsalan', 'Danil', 'Kirill', 'Sergey', 'Nikolay', 'Nasty', 'Natasha', 'Ivan', 'Igor', 'Gosha', 'Galina', 'Olya', 'Oksana', 'Oleg', 'James', 'Bill']
word_answer = random.choice(vocabulary).lower()
word_display = []
for i in range(0, len(word_answer)):
    word_display.append("_")
print(word_display)
counter = 0
life = 6
letter_if_be = False

while counter != len(word_answer) and life > 0:
    print(stages[life])
    print(word_display)
    letter = input("Буква:")
    letter_if_be = False
    for i in range (0, len(word_answer)):
        if letter ==word_answer[i]:
            if word_display[i] != "_":
                letter_if_be = True
            else:
                word_display[i] = letter
                counter += 1
                letter_if_be = True
    if not letter_if_be:
        life = life - 1
if counter == len(word_answer):
    print(word_answer)
    print("Победа")

else:
    print(stages[life])
    print("Ты помер")



