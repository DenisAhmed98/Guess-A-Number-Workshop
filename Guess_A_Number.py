import random

computer_number = random.randint (1, 100)

while True:
    player_input = input("Guess the Computers Number (1-100): ")

    player_number = int(player_input)

    if not player_input.isdigit():
        print("Invalid input! Try Again...")
        continue

    if player_number == computer_number:
        print("You Win!!!")
        break

    if player_number > computer_number:
        print("Too High!")
        continue

    if player_number < computer_number:
        print("Too Low!")
        continue