import random
import time

sequence = []

print("Memory Game")
print("Remember the numbers and enter them in the correct order.\n")

while True:
    sequence.append(random.randint(1, 9))

    print("Memorize:")
    print(*sequence)

    time.sleep(2)

    print("\n" * 30)

    guess = input("Enter the sequence separated by spaces: ")

    user_sequence = list(map(int, guess.split()))

    if user_sequence == sequence:
        print("Correct! Next round.\n")
    else:
        print("Wrong sequence!")
        print("Your Score:", len(sequence) - 1)
        break