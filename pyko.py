import random]
life = 10
length = 3
answer random.randint(100,999)
answer = str(answer)
while life:
    is_guessed = False
    print ("=" * 10)
    print("Жизней:", life)
    guess = input("Предположение:")
    if len(guess) != length or guess.isdigit():
        print("Число от 100 до 999, позязя!!1!!111!!!!")
        continue













