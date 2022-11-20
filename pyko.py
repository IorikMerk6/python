import random
life = 10
length = 3
answer = random.randint(100,999)
answer = str(answer)

while life:
    is_guessed = False
    print ("=" * 10)

    print("Жизней:", end = "")
    for _ in range(life):
        print("❤", end="")
    print()
    guess = input("Предположение:")
    if len(guess) != length or not guess.isdigit():
        print("Число от 100 до 999, позязя!!1!!111!!!!")
        continue

    if guess == answer:
        print("УРА ПОБЕДА!!!🏆❤❤🤪")
        is_guessed = True
        break
    if is_guessed == False:
        for i in range(length):
            if guess [i] == answer[i]:
                print("Fermi 🤩")
                is_guessed = True
                break
    if is_guessed == False:
        for char in guess:
            if char in answer:
                print("pico🥵")
                is_guessed = True
                break
    if is_guessed == False:
        print("Bagels😡😡😡👹")
    life -= 1
    if life == 0:
        print("Проиграл!!!Число:",answer)










