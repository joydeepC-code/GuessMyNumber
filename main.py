import random
x = random.randint(0,10)

for t in range(0, 5):
    y = int(input("Guess the number, you have 5 chances: "))

    if x == y:
        print("Correct, you have guessed the number in", t + 1, "chances")
        break

    elif y > x:
        print("Your number is too high")

    elif x > y:
        print("Your number is too low")
