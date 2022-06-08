import random
x = random.randint(1,10)

for t in range(0, 5):
    y = int(input("Guess the number, you have 5 chances, the number is between 1 - 10: "))

    if x == y:
        print("Correct, you have guessed the number in", t + 1, "chances")
        break

    if y > 10:
        print("Incorrect, the number is between 1 - 10")

    elif y > x:
        print("Your number is too high")

    elif x > y:
        print("Your number is too low")

if t == 4 and x != y:
    print("You couldn't guess the number, it was", x)
