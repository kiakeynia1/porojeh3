import random

words = ['BOOK', 'DOG', 'KIA', 'CLOCK', 'ENGINEER', 'BAG']

word = random.choice(words)

horof = len(word)

for i in range(horof):
    print("-", end=" ")

joon = 10

while joon > 0:

    user_Character = input()
    user_character_c = user_Character.upper()

    if user_character_c in word:
        print("yes")

    else:
        joon = joon - 1
        print(joon)
        print("no")

    if user_character_c == word:
        print("barande shody!!!")
        break

    